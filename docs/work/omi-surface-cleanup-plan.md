# Omi-Derived Surface Cleanup Plan

## Goal

Remove repository material copied from the upstream Omi project when it does not materially contribute to Aura, while preserving any code, assets, protocols, documentation, or integrations that Aura currently depends on.

The cleanup must be conservative. This is a provenance and scope audit, not a blind delete pass.

## Audit principles

1. **Aura-first**: retain anything required by Aura's current product, build, runtime, hardware, tests, or public documentation.
2. **Provenance-aware**: identify files that are direct Omi carryovers, fork remnants, generated vendor material, or Aura-specific work.
3. **No broken contracts**: do not remove referenced assets or modules before tracing consumers.
4. **No image replacement in this pass**: image-heavy areas may be marked for later replacement when Aura-native assets are available.
5. **Simple is better**: prefer removing dead surface area over maintaining compatibility scaffolding that Aura does not use.
6. **Document uncertainty**: ambiguous Omi-derived material is listed as review-needed rather than deleted.

## Areas to audit

### 1. Android / mobile application

Inspect:
- package/application identity
- branding, icons, splash screens, illustrations, avatars
- Omi-specific screens, copy, settings, onboarding, feature flags
- Omi-only integrations and URLs
- unused resources and generated assets
- Omi documentation embedded in the app
- dependencies imported only for Omi features

### 2. Website

Inspect:
- Omi logos, screenshots, product photography, illustrations
- Omi-specific copy, links, analytics, metadata, social previews
- legacy pages/components from the Omi site
- assets that are not used by Aura pages
- CSS/JS written only for removed Omi surfaces

### 3. Backend

Inspect:
- Omi-specific routes, models, providers, service adapters, constants
- Omi-only feature flags and integrations
- copied README/architecture claims that no longer match Aura
- dependencies used only by Omi functionality
- unused compatibility paths

### 4. Root / developer tooling

Inspect:
- Omi-specific repository documentation
- imported agent/context instructions
- stale references to Omi paths or product assumptions
- copied examples, assets, and demos with no Aura consumer

## Classification

Every candidate goes into one of four buckets:

| Bucket | Meaning | Action |
|---|---|---|
| Keep | Required by current Aura behavior or documentation | Preserve |
| Rework | Useful to Aura but still Omi-shaped | Adapt later or in a focused change |
| Remove | Omi-derived and not used by Aura | Delete |
| Review | Provenance or dependency is ambiguous | Do not delete until verified |

## Evidence required before deletion

For each removal:
- search for repository references;
- trace imports/usages for code;
- trace page/component references for assets;
- check build/deployment configuration;
- check developer documentation references;
- verify that removing it does not break a public Aura path.

## Proposed PR

Create a conservative cleanup PR containing only files classified as **Remove** with high-confidence evidence.

Do not mix:
- image replacement work,
- new feature work,
- architecture refactors,
- broad formatting,
- unrelated README changes.

## PR acceptance criteria

- Aura functionality is unchanged.
- No Omi-only dead surface remains among the high-confidence candidates selected for this PR.
- No referenced Aura assets are removed.
- Public Aura routes and developer entry points continue to resolve.
- PR body lists every deleted file/group and why it was safe to remove.
- Ambiguous material is preserved and listed for the next review.

## Expected follow-up

After this cleanup PR, run a second pass focused on **Rework** items in the Android, website, and backend layers. Rework should convert Omi-shaped interfaces into Aura-native ones rather than adding more compatibility code.

## Confirmed high-confidence cleanup candidates

These are safe to include in the first cleanup PR because they are either stale extraction/scratch material or an unused legacy CI surface, and current repository search found no Aura consumer for them:

- `scratch/framer_extracted_content.md`: raw extracted website research/scratch material; its own generator script is the only repository reference.
- `backend/.github/workflows/push_replicate.yml`: legacy deployment workflow that publishes a `basedhardware/speechbrain-vad` image; no current repository references to this workflow were found.

## Deferred, explicitly not deleted

- `backend/.env.template`: contains inherited Omi-named environment variables and a development secret-looking value. Rework, not deletion, because the backend may consume environment names today.
- `backend/utils/app_integrations.py`, `backend/models/app.py`, `backend/routers/firmware.py`: contain live code that points at the upstream repository. Rework after tracing runtime behavior.
- Android package identity `com.friend.ios` and Friend/Omi app-store references: clearly inherited branding, but changing them is an application migration, not a safe cleanup deletion.
- Website Omi copy and images: defer until Aura-native replacements are available, as requested.

## First cleanup PR contents

The first PR intentionally removes only two high-confidence unused surfaces:
- `scratch/framer_extracted_content.md`
- `backend/.github/workflows/push_replicate.yml`

Everything else remains untouched until a separate consumer/deployment migration is completed.
