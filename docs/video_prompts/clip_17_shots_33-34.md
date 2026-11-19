# 片段 17｜放低伞，让雨落下（剧本镜头 33–34）

## 片段信息

- 剧本成片区间：3:07–3:21；镜头 33 为 3:07–3:14，镜头 34 为 3:14–3:21。
- 建议设置：横屏 16:9，生成 **15 秒**；成片取约 14 秒，留约 1 秒剪辑余量。建议前约 7.5 秒完整呈现放低伞、雨落肩头，后约 7.5 秒停留在闭眼与睁眼的面部反应；具体按歌曲与动作调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图2来自上一段的实际尾帧，但当前提示仅将其作为视觉参考，不是固定首帧；如平台支持首帧控制，可另行指定并核对图片编号。
- 乐正绫已经淡出，本段不再次出现。洛天依始终握着伞：伞保持打开，缓慢移到身侧较低处，让肩膀与发梢露到雨中，不收伞、不松手。
- 雨仍持续落下；伞面声随伞移低而减弱，雨落衣物与地面的近处声音变清楚，远处城市雨声保持。歌曲后期连续对齐；声音建议后期分层制作。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰和灰色布料风衣；多视图代表同一人。
2. **图2 / Picture 2 — Shot 32 实际尾帧**：`MV/pictures/shot32_tail_reference.png`。从 `output\shot31-32.mp4` 提取；参考洛天依在透明伞下的侧脸、桥边栏杆与雨夜灯光。实际剪辑帧可能不同。

两个版本按同一顺序上传。她自然撑伞，不要求伞偏向某一侧；不使用以前有结构问题的天桥桥面候选图。桥边环境作为背景，若出现道路，车流应在桥下。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory, blue eyes and an opaque grey fabric trench coat.
<Subject 2> is the rainy bridge-side setting and close side view in <Picture 2>, with a transparent umbrella, railings and soft city lights.

summary:
[reference generation] At <Subject 2>, <Subject 1> slowly lowers her still-open umbrella to her side, allowing rain to reach her shoulder and hair. She closes her eyes, then opens them and looks quietly toward the empty space ahead.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance and grey coat; do not reproduce the multi-view reference-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Use the rainy bridge-side lighting, railings and transparent umbrella as visual guidance; the reference is not a locked first frame.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like glass and metal, clean surfaces and restrained warm reflections. Fine rain is visibly falling throughout; the nearby pedestrian bridge railing and distant city remain soft in the background.
[Shot 1] A close-to-medium side view of <Subject 1> at <Subject 2>, beginning with her holding the open transparent umbrella overhead. Without letting go or folding it, she slowly moves the umbrella down to her side so that the canopy no longer covers her shoulder and hair. Keep the hand, handle and umbrella connected throughout the complete movement. Rain visibly reaches the exposed shoulder of her grey coat and the ends of her hair; small droplets darken the fabric. She remains quietly in place. Umbrella patter softens as it moves away from above her, while rain on clothing and pavement becomes clearer; distant rain continues.
[Shot 2] At 00:07.500, cut to a close view of <Subject 1>'s face in the same position. She has the still-open umbrella lowered at her side, outside the close framing, and continues to hold its handle. Rain falls lightly onto her hair and shoulder. She gently closes her eyes for a moment, then opens them and looks toward the empty space ahead. Her expression remains restrained and her lips stay naturally closed. Hold the quiet reaction through the end; no other figure appears.

overall_soundscape: Continuous distant city rain and traffic. As the umbrella moves down, its overhead patter becomes softer and close rain on fabric, hair and pavement becomes clearer. No dialogue or dramatic sting.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 15 秒的雨夜天桥 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；上一段伞下侧脸、桥边栏杆和雨夜灯光参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–3秒：洛天依站在雨夜天桥上，手持打开的透明伞，安静望向前方。细雨落在伞面和桥边栏杆上；她轻轻握稳伞柄，准备移动伞。
2. 镜头2 3–7.5秒：近景完整表现她缓慢放低伞的动作。她始终握住伞柄，伞保持打开，从头顶慢慢移到身侧较低的位置；肩膀和发梢露出伞外。细雨落上她的灰色风衣肩头和发梢，布料逐渐被打湿。
3. 镜头3 7.5–11秒：切到洛天依的侧脸近景。她仍站在原处，放低的伞在近景画面外、仍握在手中；雨轻轻落在发梢和肩膀上，她缓缓闭上眼睛。
4. 镜头4 11–15秒：她停留片刻后睁开眼，看向面前空处，神情克制而平静。雨丝和远处柔和城市灯光仍然可见；镜头在她的神情上停留至结束。

【音频风格】
远处城市雨声和车流声持续。伞从头顶移低时，伞面近处雨声减弱，雨落衣物、发梢与地面的声音逐渐清楚。无对白，不另作配乐。

【运镜与核心约束】
先用侧面近景完整表现伞从头顶移到身侧，再切到面部近景。她一直握住伞柄，伞保持打开，不收伞、不松手；雨持续可见。乐正绫已淡出，本片段不出现其他身影；此段不要求演唱口型。
```

## 剪辑与衔接

- 已检查 `output\shot31-32.mp4` 尾帧：洛天依撑透明伞的侧脸近景，雨夜栏杆和湿润背景可见。图2为提取的实际尾帧，用于视觉参考；如选用不同剪辑点，仍需核对人物朝向与伞的位置。
- 约第 7.5 秒切面部近景，最终对齐 3:14 和实际动作；确保放低伞从开始到结束保留完整，不要剪得像伞突然消失。
- 若模型不能稳定保持手、伞柄和伞面相连，可分别生成放低伞、脸部反应；剪接前检查伞保持打开并握在手中。需要时用特写掩盖画外的伞，但不要误表示她已收伞。
- 近处伞面声减弱和雨落衣物声变清楚需后期实际铺设；远处雨持续。片段结束后仍在桥上、伞位较低，可接 35 的天桥城市远景，再由 36 的握伞准备离开。
