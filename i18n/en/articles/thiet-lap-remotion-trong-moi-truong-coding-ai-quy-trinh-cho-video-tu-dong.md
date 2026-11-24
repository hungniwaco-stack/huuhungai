---
title: Setting up Remotion in an AI coding environment: a workflow for automated video
desc: How to install Remotion, create a project, preview in Studio and render MP4 video with React code, plus rules that help AI write animation correctly.
min: 7
---
QUICK: Remotion lets you create video with React code. You create a project with `npx create-video@latest`, preview in Remotion Studio, then render to MP4 with one command. The thing to remember most: all motion must be computed from the current frame number, with no ordinary CSS animation.
## What Remotion is and what it suits
Remotion is a framework for building video with React. Each frame of the video is one render of a React component, so you write video like writing a web page: with components, with props, reusable and generated in bulk from data. This approach suits video with a repeated structure such as news bulletins, explainer videos, templated product intro clips, or video personalized for each customer. It does not replace traditional editing tools for video that needs free-form emotional cutting.
## Preparation
- **Node.js** of a recent enough version. Check the current version requirement in the Remotion documentation before installing.
- **A code editor** such as VS Code, and a terminal.
- **License:** Remotion has its own license, free in some cases, but businesses may need to buy a commercial license. Read the official terms carefully if you use it for business work.
## Step 1: Create the project
```
npx create-video@latest
```
The generator will ask for a project name and a starting template. Choose a blank or basic template to understand the structure more easily. When it finishes, go into the project folder and install the libraries if the generator has not:
```
cd project-name
npm install
```
## Step 2: Open Remotion Studio to preview
```
npm run dev
```
This command opens Remotion Studio in the browser. This is where you watch the video, drag the timeline, change props and check each frame. Each time the AI or you edit the code, Studio updates itself, so the try-and-fix loop is very fast.
## Step 3: Understand three core concepts
- **Composition:** declares a video made of a component, `fps` (frames per second), `width`, `height` and `durationInFrames` (the total number of frames).
- **useCurrentFrame():** returns the number of the frame being drawn. All motion must be derived from this value.
- **interpolate() and spring():** turn the frame number into smooth values such as opacity, position and size.
An example of a line of text fading in over the first second, for a 30 frames-per-second video:
```
import { useCurrentFrame, interpolate, AbsoluteFill } from "remotion";

export const Title = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
      <h1 style={{ opacity: opacity, fontSize: 96 }}>Hello</h1>
    </AbsoluteFill>
  );
};
```
## Step 4: Render to a video file
```
npx remotion render composition-name out/video.mp4
```
Replace `composition-name` with the id you declared in the Composition. Remotion builds each frame with a headless browser and then stitches them into a video, so the first render may need to download extra required components. Long videos and high resolution take more time.
## Important rules when letting AI write Remotion code
These are the mistakes AI makes most, because ordinary React code does not apply as is:
- **Do not use CSS transitions or animations.** They run on the real clock, while Remotion builds each frame separately, so the motion will not match. Use `useCurrentFrame()` with `interpolate()` or `spring()`.
- **Do not use plain random numbers.** `Math.random()` gives a different result each frame and causes flicker. Use Remotion's `random("seed")` function to get a fixed value.
- **Static assets** such as images and audio go in the `public/` folder and are called with `staticFile()`.
- **Use `Sequence`** to set the start time of each scene instead of adding and subtracting frame numbers yourself.
- **Fonts and images must finish loading** before rendering, or the first frame may be missing text.
## Checklist before handing work to AI
- The project runs `npm run dev` and you see the sample video in Studio.
- You have chosen the `fps`, size and length you want, and told the AI.
- You have written the rules above into a guide file for the AI to read each time.
- The project is in Git so you can undo when the AI edits wrongly.
The specific workflow for handing work to Claude Code is in [Claude Code and Remotion: making video with an AI coding workflow](claude-code-va-remotion-tao-video-bang-workflow-lap-trinh-ai.html). If you do not use Claude Code yet, first see [Setting up Claude Code step by step: the foundation for AI coding](thiet-lap-claude-code-tung-buoc-nen-tang-cho-coding-bang-ai.html).
