# 片段 12｜山坡观景台：眺望雨夜城市（剧本镜头 23–24）

## 片段信息

- 剧本成片区间：2:04–2:16；镜头 23 为 2:04–2:10，镜头 24 为 2:10–2:16。
- 建议设置：横屏 16:9，生成 **13 秒**；成片取约 12 秒，预留约 1 秒剪辑余量。建议 0:00–0:06.5 是城市大远景，0:06.5–0:13 是同一观景台的人物背影中远景；切点按音乐和画面调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片提供人物与场景参考，不是固定首帧。
- 镜头 22 已在市区公交站结束，23 通过切镜与时间省略到达山坡观景台；不需要生成两地之间的连续路程。整段雨夜、独自撑伞，不出现乐正绫身影。
- 歌曲后期连续对齐。观景台近处雨声、雨点敲伞和栏杆的声音清楚，山下车流声较远，给人声留出空间。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰发色、低位马尾、花饰和灰色布料风衣；多视图为同一人。
2. **图2 / Picture 2 — C 组山坡观景台**：`MV/pictures/C_anime_pbr/13_hillside_overlook_v2.png`。参考山坡高处观景台、林木栏杆、辽阔山下城市、高楼、霓虹、轨道列车、道路和雨夜氛围；场景图无人物，人物由图1定义。

两个版本按相同顺序上传。透明伞由提示词描述，自然撑伞；细雨始终可见，地面只保留小水洼和克制反光。镜头 23 和 24 是同一座观景台的不同景别。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the rainy hillside observation terrace from <Picture 2>, with a mountain slope, railing and high vantage point overlooking a vast Japanese city with layered high-rises, neon-lit commercial districts, railway and roads.

summary:
[reference generation] A wide view establishes <Subject 2> and the rainy city below, with <Subject 1> a small figure near the railing. A closer rear view shows her quietly looking over the city under a transparent umbrella.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character's appearance and clothing; she is a small distant figure first, then seen from behind. Do not reproduce the character-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the same terrace, railing and layered city, railway, roads and warm lights while changing camera distance.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like glass and metal, clean surfaces and restrained warm reflections. Fine rain is visibly falling across the terrace and distant city. The terrace is damp with only a few small shallow puddles.
[Shot 1] A very wide view from <Subject 2> looks out across the city below. High-rises, glowing windows and colorful neon-lit commercial districts form layers across the vast city below; an elevated train moves slowly and a few cars travel along the wet road. <Subject 1>, wearing her grey coat and holding an open transparent umbrella, stands near the railing as a small figure seen from behind. Keep the city expansive and the person small but visible. Rain falls through the city lights; the camera holds the view quietly.
[Shot 2] At 00:06.500, cut closer to a medium-long rear view of <Subject 1> at the same railing. She naturally holds her transparent umbrella above her and looks toward the rainy city. A light breeze moves a few strands of her ponytail; scattered raindrops bead and slide along the railing. City windows and distant traffic remain visible ahead. Hold the calm observation through the end; no apparition appears.

overall_soundscape: Rain falls close to the terrace, with soft drops on the umbrella and railing; city traffic and the train are distant. Keep the ambience gentle enough to leave space for the song. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 13 秒的山坡观景台眺望雨夜城市的 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；观景台栏杆、山下城市、高楼、铁路与道路参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–6.5秒：从山坡观景台望向雨夜都市的大远景。山坡上的林木与栏杆位于前景，山谷中的繁华都市一直延伸至远方；高楼灯窗、商业区霓虹层层闪耀，高架轨道上的列车缓缓经过，山下道路上有少量车辆行驶。洛天依穿着灰色风衣、撑着透明伞，背对镜头站在栏杆附近，是画面中一个小小的身影。
2. 镜头2 6.5–13秒：切到同一观景台的背影中远景。洛天依自然撑着透明伞，安静望向山下的城市；微风轻轻带动她的发梢，栏杆上的小水珠在雨中缓慢滑落。远处楼窗、轨道和车灯仍然可见，镜头停留在她看雨夜城市的背影上。

【音频风格】
近处雨声与雨点敲打伞面、栏杆的声音清楚；山下车流和列车声较远。无对白，不另作配乐。

【运镜与核心约束】
先保持城市大远景，再切近到同一观景台的背影中远景。两镜中的栏杆、城市布局和人物造型保持一致；雨丝持续可见，地面湿润，只有局部小水洼。洛天依自然撑伞，画面中不出现乐正绫身影。
```

## 剪辑与衔接

- 已检查 `output\shot21-22.mp4` 的尾帧：洛天依撑透明伞背对镜头，仍在公交站附近。可从她的背影切到观景台大远景，用连续雨声和伞面声连接，并通过切镜省略上山路程；不是同一地点的连续走路。
- 约第 6.5 秒从城市大远景切到背影中远景，最终按 2:10 的歌曲位置与画面调整；模型也可先分开生成两个景别，再从大景切近。
- 观景台参考图适用于后续 25–26，城市布局与雨夜光色尽量保持一致；实际生成后再检查栏杆、人物站位和镜头方向。
- 生成视频后检查列车是否沿轨道行驶、汽车是否位于道路、栏杆是否连续；远景不必强求微小文字或车牌可读。
