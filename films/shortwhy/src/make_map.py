#!/usr/bin/env python3
"""Render the Mercator hook map from real geometry, and measure it.

Natural Earth 110m (public domain) is used for DRAWING only. The 14x claim on
screen comes from the official published areas, not from this simplified
geometry — NE 110m is ~1% off on each figure, which compounds to 13.7.

Outputs into assets/prepared/:
  map_world.png      sea + all land, palette colours
  map_greenland.png  Greenland alone, accent, same canvas
  map_africa.png     Africa alone, accent-dim, same canvas
  map_metrics.json   pixel areas, centroids and the scale factor for the shrink
"""
import json, math, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, '..')
PREP = os.path.join(ROOT, 'assets', 'prepared')
os.makedirs(PREP, exist_ok=True)

# ---- art direction tokens (ART_DIRECTION.md is the source of truth) ----
BG      = (12, 16, 24)        # #0C1018  sea
LAND    = (49, 80, 111)       # #31506F  primary
LANDE   = (26, 38, 55)        # land edge
ACCENT  = (255, 176, 32)      # #FFB020
AFRICA  = (110, 127, 148)     # #6E7F94  secondary

# ---- framing: a vertical window holding both Greenland and Africa ----
LON0, LON1 =  -78.0,  58.0
LAT0, LAT1 =   84.0, -42.0     # top, bottom
W = 1080
SS = 2                          # supersample; PIL does not antialias polygons

# published areas (authoritative, not from the drawing geometry)
AREA_GREENLAND = 2_166_086      # Statistics Greenland
AREA_AFRICA    = 30_370_000     # commonly published continental total
RATIO = AREA_AFRICA / AREA_GREENLAND


def merc_y(lat):
    lat = max(min(lat, 85.0), -85.0)
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


Y0, Y1 = merc_y(LAT0), merc_y(LAT1)
X0, X1 = math.radians(LON0), math.radians(LON1)
H = int(round(W * (Y0 - Y1) / (X1 - X0)))


def project(lon, lat, w, h):
    x = (math.radians(lon) - X0) / (X1 - X0) * w
    y = (Y0 - merc_y(lat)) / (Y0 - Y1) * h
    return x, y


def polys(geom):
    return [geom['coordinates']] if geom['type'] == 'Polygon' else geom['coordinates']


def draw_feature(dr, feat, w, h, fill, outline=None, width=0):
    for poly in polys(feat['geometry']):
        for i, ring in enumerate(poly):
            pts = [project(lon, lat, w, h) for lon, lat in ring]
            if len(pts) < 3:
                continue
            dr.polygon(pts, fill=(BG if i else fill))
            if outline and i == 0:
                dr.line(pts + [pts[0]], fill=outline, width=width)


def render(features, w, h, fill, bg=None, outline=None, width=0):
    im = Image.new('RGBA', (w, h), (bg + (255,)) if bg else (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    for f in features:
        draw_feature(dr, f, w, h, fill, outline, width)
    return im


def alpha_stats(im):
    """Opaque pixel count and centroid, in the image's own pixel space."""
    a = im.split()[3]
    px = a.load()
    n = 0; sx = 0; sy = 0
    for y in range(im.height):
        for x in range(im.width):
            if px[x, y] > 128:
                n += 1; sx += x; sy += y
    return n, (sx / n, sy / n) if n else (0, 0)


data = json.load(open(os.path.join(ROOT, 'assets', 'raw', 'ne_110m_countries.geojson')))
feats = data['features']
greenland = [f for f in feats if f['properties'].get('NAME') == 'Greenland']
african = [f for f in feats if f['properties'].get('CONTINENT') == 'Africa']
assert greenland and african

ws, hs = W * SS, H * SS

# world plate
world = render(feats, ws, hs, LAND, bg=BG, outline=LANDE, width=2 * SS)
world.resize((W, H), Image.LANCZOS).convert('RGB').save(os.path.join(PREP, 'map_world.png'))

# isolated layers on the same canvas, so they stack without offsets
gl = render(greenland, ws, hs, ACCENT, outline=(255, 255, 255), width=1 * SS)
af = render(african,  ws, hs, AFRICA)
gl_small = gl.resize((W, H), Image.LANCZOS)
af_small = af.resize((W, H), Image.LANCZOS)
gl_small.save(os.path.join(PREP, 'map_greenland.png'))
af_small.save(os.path.join(PREP, 'map_africa.png'))

g_px, g_c = alpha_stats(gl_small)
a_px, a_c = alpha_stats(af_small)

# Scale Greenland so its DRAWN area equals Africa's drawn area / true ratio.
scale = math.sqrt((a_px / RATIO) / g_px)

metrics = {
    'canvas': [W, H],
    'window': {'lon': [LON0, LON1], 'lat': [LAT0, LAT1]},
    'greenland': {'px': g_px, 'centroid': [round(g_c[0], 1), round(g_c[1], 1)]},
    'africa':    {'px': a_px, 'centroid': [round(a_c[0], 1), round(a_c[1], 1)]},
    'mercator_inflation': round(g_px / (a_px / RATIO), 2),
    'true_ratio_africa_over_greenland': round(RATIO, 2),
    'shrink_scale': round(scale, 4),
    'translate': [round(a_c[0] - g_c[0], 1), round(a_c[1] - g_c[1], 1)],
    'areas_km2': {'greenland': AREA_GREENLAND, 'africa': AREA_AFRICA},
}
json.dump(metrics, open(os.path.join(PREP, 'map_metrics.json'), 'w'), indent=2)

print(f'canvas {W}x{H}')
print(f'Greenland drawn {g_px:,} px  centroid {g_c[0]:.0f},{g_c[1]:.0f}')
print(f'Africa    drawn {a_px:,} px  centroid {a_c[0]:.0f},{a_c[1]:.0f}')
print(f'On this Mercator, Greenland is drawn {g_px/a_px:.2f}x Africa\'s area; truly it is 1/{RATIO:.2f}.')
print(f'=> Mercator inflates Greenland {metrics["mercator_inflation"]}x relative to truth')
print(f'=> shrink scale {scale:.4f}, translate {metrics["translate"]}')
