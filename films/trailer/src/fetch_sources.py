#!/usr/bin/env python3
"""Download the six verified public-domain originals from their SOURCE INSTITUTIONS.

The collection was discovered via The Public Domain Review, which labels its rights "Various".
PDR's own guidance is to verify with the holding institution, so nothing here is taken from
PDR's CDN: each item is fetched from the Met or the Library of Congress, and the Met items are
checked for isPublicDomain before use. Art Institute of Chicago items from the same PDR
collection are deliberately absent — api.artic.edu returns HTTP 403 behind Cloudflare, so their
rights could not be verified.
"""
import json, os, ssl, sys, urllib.request

OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'raw')
ctx = ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
px = os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')
op = urllib.request.build_opener(
    urllib.request.ProxyHandler({'https': px, 'http': px} if px else {}),
    urllib.request.HTTPSHandler(context=ctx))
UA = {'User-Agent': 'documentary-research/1.0'}


def get(url):
    return op.open(urllib.request.Request(url, headers=UA), timeout=180).read()


MET = {54541: 'met54541_harunobu_kiteflying.jpg', 341621: 'met341621_downman_dyson.jpg'}
LOC = {
    '2001705764': ('loc2001705764_perkins_manlift.jpg',
                   'https://tile.loc.gov/storage-services/service/pnp/ppmsca/51600/51642v.jpg'),
    '2017645646': ('loc2017645646_perkins_broadst.jpg',
                   'https://tile.loc.gov/storage-services/service/pnp/ppmsca/51600/51641v.jpg'),
    '2008660875': ('loc2008660875_hokusai_asakusa.jpg',
                   'https://tile.loc.gov/storage-services/service/pnp/jpd/02300/02310v.jpg'),
    '2009617160': ('loc2009617160_plummer_girlkite.jpg',
                   'https://tile.loc.gov/storage-services/service/pnp/ppmsca/37400/37448v.jpg'),
}

os.makedirs(OUT, exist_ok=True)
for oid, fn in MET.items():
    d = json.loads(get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}'))
    if not d['isPublicDomain']:
        sys.exit(f'REFUSING {oid}: Met reports isPublicDomain=False')
    open(os.path.join(OUT, fn), 'wb').write(get(d['primaryImage']))
    print(f'OK  {fn}  CC0  {d["artistDisplayName"]} — {d["title"]} ({d["objectDate"]})')

for iid, (fn, url) in LOC.items():
    rec = json.loads(get(f'https://www.loc.gov/item/{iid}/?fo=json'))['item']
    adv = rec.get('rights_advisory') or ''
    if 'No known restrictions' not in str(adv):
        sys.exit(f'REFUSING {iid}: unexpected rights advisory {adv!r}')
    open(os.path.join(OUT, fn), 'wb').write(get(url))
    print(f'OK  {fn}  {adv}')
