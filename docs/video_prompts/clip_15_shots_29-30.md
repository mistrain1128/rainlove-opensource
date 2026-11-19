# 片段 15｜天桥雨雾中的相遇（剧本镜头 29–30）

## 片段信息

- 剧本成片区间：2:40–2:53；镜头 29 为 2:40–2:47，镜头 30 为 2:47–2:53。
- 建议设置：横屏 16:9，生成 **14 秒**；成片取约 13 秒，留约 1 秒剪辑余量。建议前约 7.5 秒为天桥相遇，后约 6.5 秒为两手特写；实际按动作和歌曲调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。下列图片是角色和场景参考，不是固定首帧；支持首帧控制时可另行选取实际尾帧，并核对平台的图片编号。
- 乐正绫的身影在 29 **柔和淡入一次**，连续留在桥上直到下一片段的 31 再淡出；本段结尾不要提前消失。面部被雨雾柔化，人物不化成水或碎片。
- 两人相距数米，洛天依肩后视角让距离清楚可见；后续手部镜头保持同一空间关系，伸手也无法触及。
- 雨声：她出现时近处伞面雨声渐薄，远处城市雨声持续；两人伸手时维持短暂的轻薄感，歌曲不受影响。雨声建议后期分层控制。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰和灰色布料风衣；多视图为同一人。她自然撑透明伞。
2. **图2 / Picture 2 — 乐正绫**：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。参考深红长发、发饰和深色长外套；参考图面部清晰，但本段中面容由柔和雨雾与光线遮模糊。
3. **图3 / Picture 3 — Shot 28 实际尾帧**：`MV/pictures/shot28_tail_reference.png`。从 `output\shot27-28.mp4` 提取；参考天桥栏杆、桥下道路、灯光、雨夜城市及前段洛天依所在位置。前段实际采用的剪辑帧可能不同，此图并非固定首帧。

两个提示词版本按相同顺序上传。两人是不同角色，洛天依独自撑伞；乐正绫是雨雾中单个朦胧身影。天桥横跨并高于道路，车辆在桥下行驶；不使用之前有结构问题的桥面候选图。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is Yuezheng Ling, one figure referenced from <Picture 2>, with dark red long hair and a dark long coat. The reference face is clear, but her face in this sequence is softened by rain haze.
<Subject 3> is the pedestrian overpass and rainy city shown in <Picture 3>, with railings and a road passing below the elevated deck.

summary:
[reference generation] On <Subject 3>, <Subject 2> gently fades into the rain haze once several meters in front of <Subject 1>. From behind <Subject 1>'s shoulder, the distance remains visible as she takes a few steps; both reach toward each other from far apart without touching.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): partially_preserved - Keep one character's appearance and grey coat; do not reproduce the multi-view reference sheet. Her hand extends from her grey coat sleeve.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 4]): partially_preserved - Keep her dark red hair and coat recognizable, while her face is indistinct in the rain haze. She fades in once and remains visible through the end.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): partially_preserved - Keep the elevated pedestrian deck, railings, city lights and road below; change framing from the exterior wide reference to bridge-level views. The reference is not a locked first frame.

detailed_description:
A semi-realistic Japanese anime city at rainy blue-grey night, with PBR-like glass and metal, clean surfaces and restrained warm city reflections. Fine rain visibly falls across the bridge and city. The pedestrian bridge is elevated over the road; cars travel below.
[Shot 1] A medium-wide view on the pedestrian deck of <Subject 3>. <Subject 1> stands under her open transparent umbrella. Several meters ahead, <Subject 2> softly fades into view once through the rain haze; her face remains indistinct. Nearby umbrella patter gradually grows thinner, while distant rain and traffic continue.
[Shot 2] At 00:03.000, cut behind <Subject 1>'s shoulder. Her shoulder and umbrella edge are in the foreground; <Subject 2> remains several meters away, with the wet bridge walkway and rain visible between them. <Subject 1> takes a few slow steps, but they remain far apart and cannot touch. <Subject 2> remains still and softly veiled by rain haze.
[Shot 3] At 00:07.500, cut to a close view of <Subject 1>'s hand emerging from her grey coat sleeve. She slowly extends it toward the distant figure, reaching into the rain but unable to span the several-meter distance. Her other hand continues holding the umbrella, outside the close framing.
[Shot 4] At 00:10.500, cut to a view from behind <Subject 1>'s blurred outstretched hand in the foreground toward <Subject 2> farther along the bridge. <Subject 2> gently raises her hand in response. The length of walkway and rain between them remains visible; their hands do not touch or appear side by side at the same depth. <Subject 2> remains present through the end, softly veiled by rain haze.

overall_soundscape: Continuous distant city rain and traffic below the bridge. Nearby umbrella rain gradually thins as the figure appears and remains light during the reaching hands; do not silence distant rain. No dialogue or dramatic sting.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 14 秒的雨夜天桥 MV 片段。洛天依的外貌和灰色风衣参考图1；乐正绫的深红长发与深色长外套参考图2；天桥栏杆、桥下道路和雨夜城市参考图3。图2面容清晰，但片中乐正绫的面庞被雨雾柔和遮模糊。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–3秒：雨夜人行天桥中远景。洛天依自然撑着透明伞站在桥上；前方数米外的雨雾里，乐正绫的身影缓缓淡入，身影朦朦胧胧，隐约可辨，面容朦胧。细雨持续落下，桥下道路有远处车流。
2. 镜头2 3–7.5秒：切到洛天依肩后视角。她的肩膀和伞沿位于前景；乐正绫站在数米之外，两人之间的湿润桥面和雨丝清楚可见。洛天依慢慢向前走几步，乐正绫留在原处；即使走近，两人仍相距很远，无法触及。
3. 镜头3 7.5–10.5秒：切到洛天依的手部特写。灰色风衣袖口旁，她朝远处的乐正绫缓缓伸出一只手，手伸入雨中，却够不到仍在数米外的身影。另一只手继续握伞，位于特写画面之外。
4. 镜头4 10.5–14秒：从洛天依伸出的手后方望向桥的另一端，前景的手轻微虚化；远处的乐正绫抬起一只手回应。两人之间仍隔着数米长的桥面和雨丝，双手没有碰到，也不并排出现在同一近景平面上。她的身影保持到片段结束。

【音频风格】
雨和桥下远处车流声持续；乐正绫淡入时，近处伞面雨声逐渐变薄，远处雨声保持。两人伸手时近处雨声仍轻薄，无对白，不另作配乐。

【运镜与核心约束】
从天桥中远景切到洛天依肩后视角，再切到她的手，最后以前景虚化的手和远处的乐正绫共同呈现两人之间的距离。两人始终相距数米，伸手也无法触及；雨丝始终可见。人行桥位于道路上方，车辆在桥下。乐正绫只淡入一次，本片段内不淡出或化作水滴；她的面庞始终朦胧。
```

## 剪辑与衔接

- 已检查 `output\shot27-28.mp4` 尾帧：洛天依独自站在横跨道路的人行桥上，车辆从下方通过。图3是提取的实际尾帧，可用于约束桥体和灯光；按当前 Ref2VA 提示它不是固定首帧。
- 约第 3 秒切洛天依肩后视角，第 7.5 秒切她的手，10.5 秒以前景手和远处身影同框；最终按 2:47 的唱句和可用动作调整，预留约 1 秒剪辑余量。
- 身影只在 29 淡入一次，30 中保持出现，下一段 31 才缓慢淡出。只让近处伞面雨声渐薄，远处城市雨与歌曲保持。
- 若模型混淆手的归属或提前让角色消失，可分别生成肩后远近同框、洛天依伸手和远处乐正绫抬手，再后期切镜；用桥面或前后景保持数米的距离感，不接触。
- 补充桥面视角时仍需核对桥面横跨道路、车辆在下，及楼梯与人行道连接；不以之前不合格的桥面参考图当作已验证结构。
