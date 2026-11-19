# 片段 18｜雨夜天桥与准备离开（剧本镜头 35–36）

## 片段信息

- 剧本成片区间：3:21–3:31；镜头 35 为 3:21–3:27，镜头 36 为 3:27–3:31。
- 建议设置：横屏 16:9，生成 **11 秒**；成片取约 10 秒，预留约 1 秒剪辑余量。前约 6.5 秒以天桥大远景和栏杆细节呈现城市，后约 4.5 秒保留握伞与转身动作；最终按歌曲与生成动作调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片提供角色、天桥和前段画面的参考，不是固定首帧。
- 时段是雨夜向黎明过渡：天空从深蓝稍稍转为灰蓝，城市灯光仍明亮、雨仍在下。远景呼应镜头 28，桥上只有洛天依，不再出现乐正绫身影。
- 上一段按剧本将打开的伞放低到身侧。保持伞在手中且打开，本段只握稳伞柄、转身准备离开；**不要提前在本段把伞举回头顶**，该动作留给镜头 37。
- 远处城市雨声和车流声连续，近处雨落衣物与地面仍可听见。歌曲后期连续对齐；本段无对白，不生成新配乐。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰与灰色布料风衣；多视图为同一人。
2. **图2 / Picture 2 — Shot 28 天桥远景**：`MV/pictures/shot28_tail_reference.png`。参考桥横跨道路、桥下车流与城市构图；本段仅一人，天光可比该图略微转灰蓝。
3. **图3 / Picture 3 — Shot 34 实际尾帧**：`MV/pictures/shot34_tail_reference.png`。从 `output\shot33-34.mp4` 提取，参考人物被雨打湿的侧脸、桥边栏杆和雨夜光线；尾帧没有拍到伞，不能仅凭此帧确认伞在画外的位置。

两个模型版本按相同顺序上传。图2、图3仅作视觉参考，不锁定首帧；图2此前有人物撑伞在头顶，而本段的伞应遵循文字描述，保持打开、放低并握在手中。桥体跨越道路，车辆在桥下行驶。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is the pedestrian overpass and rainy city in <Picture 2>, showing a raised walkway crossing above a road with vehicles below.
<Subject 3> is the preceding close-up in <Picture 3>, used for the wet hair, grey coat, bridge-side lighting and emotional continuity; the umbrella is outside this reference frame.

summary:
[reference generation] A wide view of <Subject 2> echoes the earlier bridge composition with <Subject 1> alone in the rain. A brief railing detail carries the city lights into a close view as she steadies her lowered open umbrella handle and turns to prepare to leave.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): partially_preserved - Keep one character's appearance and clothing; show her small in the wide view, softly out of focus behind the railing, and her hand at the umbrella handle in the close view. Do not reproduce the reference-sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3]): partially_preserved - Keep the raised bridge crossing above the road and the rainy city; preserve the bridge's relationship to traffic while the sky becomes slightly greyer.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): partially_preserved - Retain her wet hair and coat and restrained mood, without treating this close-up as a fixed first frame.

detailed_description:
A semi-realistic Japanese anime city in rain before dawn, with PBR-like glass and metal, clean surfaces and restrained warm city reflections. The deep-blue sky begins to shift subtly toward grey-blue; city lights remain on. Fine rain visibly falls throughout.
[Shot 1] A wide exterior view of <Subject 2>, echoing the raised bridge crossing in <Picture 2>. The pedestrian deck clearly crosses above the roadway, with cars traveling below and illuminated high-rises beyond. <Subject 1> stands alone as a small figure on the bridge, her wet grey coat and hair catching the rain. She holds an open transparent umbrella lowered at her side, no longer covering her shoulders; do not copy its overhead position from the reference. There is no other figure or apparition on the bridge. A distant train passes on the separate elevated railway as the camera gently drifts sideways, keeping the bridge and road clearly visible.
[Shot 2] At 00:04.000, cut to a close view of the wet bridge railing. A raindrop slides along the metal while warm and cool city lights blur softly beyond; <Subject 1> is alone and softly out of focus farther along the bridge. Rain continues visibly falling.
[Shot 3] At 00:06.500, cut to a close view of <Subject 1>'s hand on the handle of the same open umbrella, still held low beside her. Water beads on her sleeve and the handle. She gently steadies her grip and begins to turn her body toward the bridge exit, preparing to leave. Keep the handle connected to her hand; do not fold, release or raise the umbrella overhead yet. Hold briefly on the turn and falling rain.

overall_soundscape: Continuous broad rain and distant city traffic beneath the bridge; nearer rain on clothing and pavement remains audible through the close-up. No dialogue or dramatic sting.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 11 秒的雨夜天桥 MV 片段。洛天依的外貌、发型和灰色风衣参考图1；天桥横跨道路的远景构图与城市参考图2；上一段打湿的发梢、侧脸和雨夜光线参考图3。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–4秒：切到雨夜天桥与城市的外部远景，呼应图2的构图。人行桥面横跨在公路上方，车辆沿桥下道路行驶，远处高架轨道上有一列亮着灯的列车经过，高楼灯光仍然明亮。洛天依独自站在桥上，是画面中小小的身影；打开的透明伞放低在身侧，雨落在她的肩头与发梢。镜头轻轻横移，深蓝天空开始略微转为灰蓝。
2. 镜头2 4–6.5秒：切到湿润的天桥栏杆近景，一颗水珠沿栏杆缓缓滑动；远处暖色与冷色城市灯光柔和虚化。洛天依独自站在桥上，在栏杆后方轻微虚化，细雨持续落下。
3. 镜头3 6.5–11秒：切到洛天依握伞柄的手部近景。雨水落在袖口与伞柄上，她轻轻握稳手中的伞，转身准备朝天桥出口走去。伞仍保持打开并放低在身侧，她没有松手，也没有在本镜中将伞举回头顶；镜头在这个动作上稍作停留。

【音频风格】
开阔的雨声与桥下远处车流声持续；近景中雨落衣物和地面的声音稍微清楚。无对白，不另作配乐。

【运镜与核心约束】
从天桥城市远景切到栏杆水珠，再切至握伞柄的手。人行桥面横跨道路并高于车流，列车行驶在远处独立的高架轨道上；画面中只有洛天依一人。雨丝持续可见，地面湿润且只有局部小水洼。天空只是从夜色略微转灰蓝，不突然切成明亮白天。
```

## 剪辑与衔接

- 已检查 `output\shot33-34.mp4` 尾帧：洛天依被雨打湿的侧脸近景、桥边栏杆及雨夜背景；伞不在画面内，无法从尾帧确认它的位置。本段根据剧本和上一段的预期动作接为“伞打开、放低且仍握在手中”，生成后需结合实际剪辑点核对。
- 图2来自 Shot 28 的实际尾帧，桥体构图用于呼应；图中伞在头顶，本段应改为身侧放低，不能把图2直接当作无需修改的固定首帧。图3仅供人物侧脸与雨夜光线参考。
- 约第 4 秒切栏杆水珠、6.5 秒切伞柄，最终按 3:27 唱句与动作调整。若远景无法清楚表达伞位，可将伞位交给后续近景确认；注意手、伞柄与伞始终连贯，避免瞬间出现第二把伞。
- 三个景别共用 11 秒，栏杆细节只作短暂呼吸，握伞与转身留出完整动作；如果生成过于拥挤，可单独生成栏杆水珠，后期选择插入。
- 片尾只转身准备离开；下一段镜头 37 再下桥，并把此前放低的伞重新撑到头顶。天桥跨道路和车辆在桥下的结构仍需逐镜检查。
