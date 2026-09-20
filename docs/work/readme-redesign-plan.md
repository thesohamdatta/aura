# README Redesign Plan

## Goal

Rebuild the root README as the public front door to Aura: credible to engineers, legible to new visitors, and useful to founders, researchers, and technical evaluators without becoming a product brochure.

## Evidence gathered

- The current README is compact but visually centered on a single hero image and has broken/nonexistent documentation links for several setup guides.
- Aura already has a structured documentation surface under `website/docs.html` and developer documentation under `docs/developer/`.
- The Omi repository uses a strong README pattern: one-line positioning, clear external links, quick start, developer entry points, architecture, hardware/build references, contribution guidance, and licensing. We will borrow the information architecture, not the copy.
- The current Aura website docs expose a Build Manual covering build path, hardware, firmware, backend, app, AI providers, memory/RAG, troubleshooting, and FAQ.

## Audience jobs

### New visitor

In the first 30 seconds they should understand:
1. what Aura is;
2. why it exists;
3. what is open source;
4. where the project currently stands;
5. where to learn more.

### Developer

They should be able to:
1. identify the repository areas;
2. choose hardware, firmware, app, or backend work;
3. jump into the correct documentation;
4. understand the architecture at a glance;
5. find contribution and safety guidance.

### Technical evaluator / founder / investor

They should be able to see:
1. product thesis;
2. system architecture;
3. open-source scope;
4. technical differentiators;
5. current build status and limitations;
6. project documentation and source evidence.

## README structure

1. **Wordmark and positioning**
   - Aura name
   - concise screenless/ambient-AI statement
   - avoid decorative hero image

2. **Navigation row**
   - Website
   - Documentation
   - Build Guide
   - Contributing
   - License

3. **What is Aura?**
   - product definition
   - problem/context
   - open-source thesis

4. **Why Aura**
   - screenless interaction
   - ambient capture
   - searchable memory
   - multimodal sensing
   - open hardware/software

5. **How it works**
   - compact architecture diagram in Markdown
   - device -> transport -> backend -> memory -> app
   - clearly distinguish current implementation from intended direction

6. **Repository map**
   - backend
   - firmware
   - app
   - hardware
   - website/docs
   - agent/developer tooling

7. **Build / Run paths**
   - Build the hardware
   - Flash firmware
   - Run backend
   - Build app
   - Keep commands minimal and link deeper guides

8. **Developer documentation**
   - central docs entry
   - developer docs
   - backend docs
   - firmware docs
   - app docs
   - architecture/context docs

9. **Hardware**
   - verified high-level component table
   - case/STL
   - avoid unsupported cost/runtime claims

10. **AI / memory architecture**
    - transcription
    - vision
    - reasoning
    - retrieval/memory
    - note provider-dependent behavior

11. **Project status**
    - explicitly label prototype / active development state
    - distinguish implemented, experimental, and planned where evidence exists

12. **Contributing**
    - concise contribution path
    - link CONTRIBUTING.md
    - link issues / PR workflow

13. **License / Security / Code of Conduct**

## Image decision

Remove the existing README hero image as requested.

Do not replace it with a decorative illustration yet. The README should remain strong with typography, tables, and an architecture diagram. A visual can be introduced later only if it communicates real system structure or hardware information.

## Quality gates

- No broken relative links.
- No links to nonexistent `docs/guides/*` paths.
- No claims copied from stale docs without evidence.
- No investor-facing hype or unverifiable market claims.
- No unnecessary duplicate documentation.
- Keep README skimmable. Detailed implementation belongs in linked docs.
- Preserve the canonical documentation graph created by the Markdown engineering work.

## Implementation sequence

1. Replace README.MD with the redesigned public/developer README.
2. Add a compact canonical documentation index link structure.
3. Update only links proven to exist.
4. Verify the resulting diff and all referenced repository paths.
5. Record the README change in the PR/work artifact.

## Success criterion

A reader can move from README -> product understanding -> architecture -> exact developer entry point without guessing which documentation is current.
