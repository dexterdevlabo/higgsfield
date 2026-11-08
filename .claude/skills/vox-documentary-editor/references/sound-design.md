# Sound Design & Editing Rhythm

Sound is half the perceived production value and most of the perceived pace. It supports the
narration; it never competes with it.

## Sonic palette

Declare a character in `ART_DIRECTION.md`, e.g. "dry, close, low-mid, mechanical." Build from:
subtle whooshes · paper and card movement · camera shutter and mechanism sounds · mechanical
and industrial textures · atmospheric room and place tone · period-appropriate ambience ·
low-frequency impacts · restrained musical stings at structural boundaries.

Source from freely licensable libraries (Freesound with per-file licence checks, BBC Sound
Effects under its terms, archive.org) or synthesise. Log every sound effect and music cue in
`ASSETS.md` with its licence, exactly like images.

## Synchronisation

Attach sound to motion, not to the timeline grid. Sync points:

| Event | Sound | Offset |
|---|---|---|
| Graphic/image reveal | short air swell | 60–80ms before the visual starts |
| Type entrance | soft tick or click | on the first frame of movement |
| Map zoom | rising filtered whoosh | starts with the zoom, tail resolves on arrival |
| Transition | directional whoosh matching the motion | leads the cut by 2–3 frames |
| Camera impact / hard push | transient + short sub | on frame |
| Highlight / annotation draw | thin pencil or electrical tick | on draw start |
| Key statistic landing | sub impact, 40–60Hz, short | on the stressed syllable |
| Act break | sub impact + silence | on the cut |

A sound effect that is not attached to an on-screen event is noise. Maximum roughly one
designed effect every 2–3 seconds; a dense film becomes exhausting and the important hits
stop registering.

## Music

Use music structurally, not continuously. One bed per act, with a deliberate change at act
boundaries. Duck music 6–9dB under narration with a 200ms attack and 400ms release. Remove
music entirely for the film's single most important statement — silence is the strongest
emphasis available.

Never use a track whose rhythm fights the narration's cadence, and never let a music cue end
mid-sentence.

## Mix targets

- Narration: −16 LUFS integrated for the programme, true peak ≤ −1.5 dBTP.
- Narration dialogue bus: −18 to −14 LUFS short-term, compressed gently (3:1, slow attack).
- Music bed: −30 to −26 LUFS under speech; −20 LUFS when exposed.
- Designed effects: −24 to −18 LUFS; sub impacts may peak higher but must not clip.
- High-pass narration at 80Hz; high-pass effects at 60Hz except deliberate sub hits.
- Short-form may be mastered to −14 LUFS for platform loudness normalisation.

```bash
# Measure and normalise
ffmpeg -i mix.wav -af ebur128=peak=true -f null -                 # measure
ffmpeg -i mix.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 -c:a pcm_s24le mix_norm.wav
# Duck music under VO (sidechain)
ffmpeg -i music.wav -i vo.wav -filter_complex \
 "[0:a][1:a]sidechaincompress=threshold=0.05:ratio=8:attack=200:release=400[m];[m][1:a]amix=inputs=2:normalize=0" \
 -c:a pcm_s24le bed.wav
```

## Editing rhythm

Pace is a function of information density, not of a target cut length.

- A shot lasts as long as its idea takes, plus 400ms of hold. Typical explainer range:
  1.8–4.5s for graphic shots, 3–8s for photographic and atmospheric shots.
- Vary it. Three equal-length shots in a row reads as a slideshow; follow a run of fast
  graphic cuts with one long breathing shot.
- Give the viewer a pause after every genuinely new or difficult idea: 0.6–1.2s with no new
  information entering, often on a held image.
- Cut on the breath in the narration, not mid-word, and not exactly on every full stop.
- Place the hook in the first 8 seconds for YouTube, the first 1.5 seconds for short-form.
- Never cut during a camera move unless the move continues across the cut.
- Audio leads picture by 2–3 frames at transitions; this is what makes a cut feel intentional.
