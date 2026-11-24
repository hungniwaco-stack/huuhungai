---
title: Hermes AI Video Generator: making explainer videos with Manim
desc: A workflow for using an agent like Hermes to write Manim scenes and build explainer videos: installing Manim, a sample scene, render commands and QA.
min: 8
---
QUICK: Manim is a Python library that builds math and explainer videos in code. You install Manim, let the agent write the scene files, run the render command itself and then review the result. The agent helps write and fix quickly, but you remain the one who checks that the content is correct and the pacing works.
## What Manim is
Manim (the community version, Manim Community Edition) is a Python library for creating animations, commonly used for math and science explainer videos. Each video is one or more Scene classes in Python, in which you declare shapes, text, formulas and movements. This approach gives precise, repeatable results, which suits structured explainer videos.
## Preparing the environment
Manim's documentation explains how to install it with `uv`. The main points:
- **Python and uv:** install `uv`, then create a project and add Manim.
- **LaTeX (optional):** only needed when you want to typeset formulas in proper math style. Plain text does not need LaTeX. Use MiKTeX on Windows, MacTeX on macOS and TeX Live on Linux.
- **System libraries (macOS, Linux):** you need Cairo, Pango and build tools. On Windows, if it reports a missing Microsoft C++, install Microsoft C++ Build Tools.
```
uv init manimations
cd manimations
uv add manim
uv run manim checkhealth
```
The last command checks the installation. If you already have a Python environment, the shorter way is `pip install manim`.
## The first sample scene
Create a file `main.py`:
```
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
```
Then render:
```
manim -pql main.py CreateCircle
```
The `-p` flag opens the video after it is built, and `-ql` chooses low quality for fast builds. Use higher quality only once the content is settled.
## The role of an agent like Hermes
An agent can write scenes from your script, fix errors when the render reports them and iterate quickly. As for Hermes Agent, Nous Research's official documentation describes it as an agent with skills and memory that you can extend with skills you create. At the time I checked, Hermes's optional skills catalog **has no dedicated skill for Manim**; the video-related skills cover other tools such as building video from HTML. So the practical approach is to write your own guide (or your own skill) describing Manim conventions for the agent. See Hermes's "Creating Skills" documentation for how.
## Suggested workflow
1. **Write a script** by scene: one idea per scene, with narration or on-screen text.
2. **Give each scene to the agent**, along with conventions: frame size, colors, fonts, duration.
3. **Render a low-quality version** to review quickly.
4. **Review the content:** are the formulas, figures and terms correct? This is where an agent easily errs and you must check.
5. **Adjust the pacing:** do transitions move too fast, and does text stay long enough to read?
6. **Stitch the scenes and render in high quality**, adding narration and music with a separate editing tool.
## Tips to help the agent write better Manim
- Give it a working sample scene and ask it to follow the same style.
- Keep one scene per file so it is easier to edit and to isolate errors.
- Ask it to run the render command itself and read the error messages before saying it is done.
- Use low quality while iterating and high quality when finished.
## Notes on content and copyright
An explainer video is only valuable when it is correct. Verify each claim yourself, especially formulas and figures. Images, music and fonts must be properly licensed. If the video is a commercial product, check the terms of each tool you use.
For building video a different way, with React code instead of Python, see [Setting up Remotion in an AI coding environment: a workflow for automated video](thiet-lap-remotion-trong-moi-truong-coding-ai-quy-trinh-cho-video-tu-dong.html).
