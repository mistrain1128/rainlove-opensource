# 片段 13｜雨夜城市与栏杆滴水（剧本镜头 25–26）

## 片段信息

- 剧本成片区间：2:16–2:28；镜头 25 为 2:16–2:22，镜头 26 为 2:22–2:28。
- 建议设置：横屏 16:9，生成 **13 秒**；成片取约 12 秒，预留约 1 秒剪辑余量。建议前 6.5 秒为城市远景组接，后 6.5 秒为观景台伞柄与栏杆滴水近景；具体切点按歌曲和画面调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图用于人物与场景，不是固定首帧。
- 城市保持山坡高处俯瞰的广阔构图，呈现日本动漫都市的霓虹与繁华。雨丝持续可见，地面只保留局部水迹与小水洼。
- 歌曲后期连续对齐；观景台近处雨声与栏杆滴水、山下远处车流分层处理，最后可逐渐引入市区车辆声。本段不出现乐正绫身影。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰低位马尾、花饰和灰色布料风衣；多视图是同一人。
2. **图2 / Picture 2 — C 组山坡观景台**：`MV/pictures/C_anime_pbr/13_hillside_overlook_v2.png`。参考山坡树林、栏杆、高处俯瞰关系，以及山下霓虹商业区、高楼、铁路和道路布局；城市细节镜头可适当改变景别。

两个版本按相同顺序上传。透明伞由提示词描述，洛天依自然撑伞。23–24 已生成，本段与它采用同一观景台；最终以生成结果检查城市方向、栏杆样式和人物位置。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy mountain observation terrace and city view from <Picture 2>, with its railing, wooded slope and expansive Japanese city below, including neon-lit high-rises, railway and roads.

summary:
[reference generation] From <Subject 2>, the view moves across the rainy neon city, railway and roads. Back at the same terrace, <Subject 1> gently holds her umbrella handle while a raindrop slides from the railing, leaving a transition to the city below.

retention_analysis:
<Subject 1> (appears in [Shot 3], [Shot 4]): partially_preserved - Keep one character's grey coat and hand holding the umbrella handle; do not reproduce the character-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): partially_preserved - Keep the high hillside vantage point, railing, wooded slope, layered city and neon lighting while changing the camera framing.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night with PBR-like materials, clean surfaces and restrained reflections. Fine rain is visibly falling throughout. The city below is vast, bright and lively, with coordinated blue, violet, cyan and warm-gold lights; the terrace remains damp with only small patches of water.
[Shot 1] A wide view from <Subject 2> looks across the illuminated city below the wooded mountain. The camera moves gently over layered high-rises, neon-lit commercial streets and distant windows, keeping the terrace's elevated vantage point clear. Rain and haze soften the far distance without obscuring the city.
[Shot 2] At 00:03.500, cut to another distant view from the same hillside. A lit train moves along its elevated railway and small vehicles travel on the road below; the road, train tracks and buildings remain distinct and grounded in the city. Rain falls visibly across the lights.
[Shot 3] At 00:06.500, cut back to a close view of <Subject 1> at the same terrace railing. In her grey coat, she gently holds the handle of her open transparent umbrella and looks toward the city. Keep the hand, umbrella handle and railing clear while the neon city is softly out of focus beyond her.
[Shot 4] At 00:10.000, cut to raindrops beading on the railing. One drop slides along the wet metal and falls, with distant city lights visible beyond. Hold the soft glow and falling rain briefly to the end; no apparition appears.

overall_soundscape: Steady rain on the terrace and distant city traffic continue; the close drop on the railing becomes clear near the end. Distant road sound may gradually become more present for the following edit. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 13 秒的山坡观景台与雨夜城市 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；山坡观景台、树林、栏杆、山下城市、铁路与道路参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–3.5秒：从山坡观景台眺望雨夜都市。远处高楼、明亮楼窗与商业区霓虹层层延伸到山谷深处，城市繁华而辽阔；细雨落在画面前景，远处有柔和雨雾。
2. 镜头2 3.5–6.5秒：切到同一观景台望出去的城市远景。亮着灯的列车沿高架轨道行驶，山下道路上有车辆经过；霓虹和暖色楼窗在雨夜里闪耀。
3. 镜头3 6.5–10秒：切回观景台近景。洛天依身穿灰色风衣，自然撑着透明伞，轻轻握住伞柄，望向山下的城市。栏杆与她的手清楚可见，远处城市灯光柔和虚化。
4. 镜头4 10–13秒：切到湿润栏杆特写。雨珠在栏杆表面聚集，其中一滴缓缓滑落、离开栏杆；背景保留朦胧的城市灯光，细雨继续落下。

【音频风格】
雨声贯穿，远处车流和列车声隐约可闻；栏杆滴水近景中，近处水滴声变得清楚。无对白，不另作配乐。

【运镜与核心约束】
从山坡俯瞰的城市大远景切到铁路与道路，再切回伞柄和栏杆滴水。保持与图2相同的观景台和城市方向；车辆在道路上、列车在轨道上。雨丝持续可见，地面湿润且只有局部小水洼；洛天依自然撑伞，不出现乐正绫身影。
```

## 剪辑与衔接

- 已检查 `output\shot23-24.mp4` 尾帧：洛天依撑透明伞，背对镜头站在山坡栏杆旁，面向霓虹城市。25 可从她的背影切至城市视野；本段参考图不是固定首帧，实际成片位置和方向仍需核对。
- 约第 3.5 秒切铁路与道路、第 6.5 秒切回伞柄、第 10 秒切栏杆滴水；最终按 2:22 的歌曲切点和可用动作调整。
- 镜头 26 结束后，通过滴水或相似方向的城市车灯切回市区的天桥楼梯，省略从山坡下山的路程；不将观景台与天桥设定为紧邻地点。
- 若模型难以稳定表现列车、车辆或栏杆上的雨滴，可将城市景观和栏杆滴水分开生成，再后期剪接。生成后检查列车在轨道上、车辆在道路上。
