---
title: Claude Code and Remotion: making video with an AI coding workflow
desc: A workflow for handing Claude Code the job of building video with Remotion: the guide file, how to write requests, the preview loop and the errors to check.
min: 7
---
QUICK: To get Claude Code to build video with Remotion effectively, write the Remotion rules into `CLAUDE.md`, hand off one scene at a time with clear parameters (fps, size, duration), check the result in Studio after each step, and render only when the preview is right.
## Why a separate workflow is needed
Claude Code writes React code very well, but video is a different genre: time is counted in frames, motion must be determined in advance, and errors often show up only when you watch. If you just command "make a product intro video", you will get code that runs but with pacing that is hard to use. The workflow below turns that into small steps with checks. This article assumes you already have a working Remotion project; see [Setting up Remotion in an AI coding environment: a workflow for automated video](thiet-lap-remotion-trong-moi-truong-coding-ai-quy-trinh-cho-video-tu-dong.html) if not.
## Step 1: Write CLAUDE.md for the video project
This file helps Claude Code remember Remotion's constraints every time it starts. A short version should include:
```
# Remotion video project
- All motion must use useCurrentFrame() with interpolate() or spring().
- No CSS transition/animation and no Math.random() (use Remotion's random()).
- Default: 1920x1080, 30 fps.
- Images and audio go in public/, referenced with staticFile().
- Each scene is its own component in src/scenes/, joined with Sequence.
- Preview with: npm run dev. Render only when I ask.
```
This is an illustrative example; adjust it to your project.
## Step 2: Prepare the inputs before calling the AI
A good video starts from clear content, not from code. Prepare:
- **A short script:** one line per scene, with the text content and the visual idea.
- **The duration of each scene** in seconds (Claude Code converts to frames itself).
- **Assets:** logo, images, music and fonts placed in `public/`.
- **Style:** main colors, fonts, whether scene transitions are fast or slow.
## Step 3: Hand off one scene at a time
Do not ask for the whole video at once. Make the first scene, watch, fix, and only then move to the next:
```
Create scene 1 in src/scenes/Intro.tsx: dark blue background, the title "Product launch"
fading in over 1 second and then holding, scene total 4 seconds at 30 fps.
Use interpolate, no CSS animation. Do not add it to the main video yet.
```
A good request has all of: the file name, content, duration, the technique to use, and the scope (not joined yet, not rendered). When Claude Code finishes, you watch it in Studio rather than only reading the code.
## Step 4: The watch and adjust loop
For each scene, check in this order in Studio:
1. Drag the timeline slowly across the whole scene, looking for flicker or stutter.
2. Look at the first and last frames, because missing text or missing images often show up there.
3. Check whether text overflows the frame or is too small when viewed on a phone.
4. If the motion is not right, describe the feeling you want in words, for example "come in fast then slow down" rather than numbers.
Change only one thing per round so you know which change caused which result.
## Step 5: Join the scenes and render
When the scenes are good, ask Claude Code to join them with `Sequence` in a main Composition, then run the render command yourself:
```
npx remotion render composition-name out/video.mp4
```
It is better for you to be the one to render because this command uses machine resources and time.
## Common errors when you let AI make video
- **Motion does not match when rendered:** usually caused by CSS animation. Repeat the rule in `CLAUDE.md`.
- **Random flickering effects:** caused by plain random numbers.
- **Font missing in the first frame:** the font had not finished loading at render time.
- **Wrong duration:** confusing seconds and frames. Always state duration in seconds with the fps.
- **Edits spreading to other scenes:** the request was too broad. Limit the scope by file name.
## Notes on cost and copyright
If you use the tool for commercial video, read Remotion's license terms. Music, images and fonts must be properly licensed. The look and content of the video are your responsibility, not the AI's, so review everything before publishing.
