# Templates

Copy this directory into a new project under `films/<name>/`, then:

1. Fill `PROJECT.md` — **age band first**, then the fact-check table.
2. Write `SHOTLIST.md`, marking every beat GENERATED or DRAWN.
3. Fill the budget table and **get approval before any paid call**.
4. Generate: one batched image call, one voiceover call. Put results in
   `assets/generated/` and `assets/vo.wav`.
5. Edit `src/index.html` (from `composition.html`) and `src/audio.py`.
6. `bash build.sh`.

`composition.html` renders as-is with the placeholder art in `assets/`, so you can see the
shape of a finished short before spending anything. It was rendered and QC-passed when
written — 468 frames, 1080×1920, captions verified present.

Two defects were found and fixed in it during that check, both worth knowing because they
fail silently:

- A `gsap` `fromTo` from `opacity: 0` is still 0 **at** its start time, so a scene whose
  first element fades in opens on an empty frame. Every scene here keeps one element
  statically visible and animates only scale or position.
- `#cap` needs a `z-index` above every scene. Without one the opaque scene backgrounds hide
  the captions and the film ships uncaptioned with no error anywhere.
