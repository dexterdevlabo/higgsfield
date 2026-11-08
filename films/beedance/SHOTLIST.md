# Shot list — How a bee draws a map

44.0s · 1320f · 30fps · 1080×1920. Safe core: x 65–950, y 270–1420.
**3 GENERATED · 1 reuse · 5 DRAWN.**

| # | In–Out | VO | On screen | Source | Motion |
|---|--------|----|-----------|--------|--------|
| 1 | 0.0–3.7 | found a field of flowers | sunlit meadow, one bee | **GEN-2** | Ken Burns 1.00→1.08, drift left |
| 2 | 3.7–7.7 | tell the others, in the dark | hive interior, comb, dim | **GEN-1** | slow push in, 1.00→1.06 |
| 3 | 7.7–11.7 | so she dances | bee mark starts moving on comb | DRAWN | figure-8 path begins tracing |
| 4 | 11.7–17.5 | a figure of eight | the full figure-8 draws itself over a hex grid | DRAWN | stroke draw-on, 2 loops |
| 5 | 17.5–23.8 | the clever part / the tilt is the way | bee on comb, **angle overlay** | **GEN-3** + DRAWN | overlay angle arc + arrow |
| 6 | 23.8–29.0 | straight up = toward the sun | sun top, hive below, vertical arrow, 0° | DRAWN | arrow rises, sun pulses once |
| 7 | 29.0–34.5 | longer waggle = further | duration bar grows; distance marker slides out | DRAWN | bar + marker, synced |
| 8 | 34.5–39.8 | von Frisch, Nobel Prize | name card, 1973, no portrait | DRAWN | type rise, rule draws |
| 9 | 39.8–44.0 | a bee drew a map, in the dark | **re-crop of GEN-1**, tight, + closing line | reuse (free) | slow push, type over |

## Reuse
Beat 9 is GEN-1 at a tighter crop and lower brightness. No generation.

## Dwell check (6–9 band, min 1.8s)
Every caption's dwell is computed in the composition as `max(1.8, 0.6 + 0.25 × words)`.
The longest line (13 words) gets 3.85s; beat 5 is sized to hold it.

## Safe area
All type sits inside x 65–950, y 270–1420. The right 130px stays clear for TikTok's action
rail. Render once with `data-guides="on"` and check before delivery.

## Why beats 3–8 are drawn
They are the lesson. A generated image cannot hold a correct angle, a legible axis or a
number that counts — and it would cost money to be worse. The diagram *is* the content.
