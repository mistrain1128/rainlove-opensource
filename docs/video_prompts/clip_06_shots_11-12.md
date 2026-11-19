# 片段 06｜雨滴中的家（剧本镜头 11–12）

## 片段信息

- 剧本成片区间：0:50–1:02；镜头 11 为 0:50–0:56，镜头 12 为 0:56–1:02。
- 推荐设置：横屏 16:9，**合并为一段生成，时长 14 秒**。前后两部分各安排约 7 秒；最终按歌曲与画面节奏剪成约 12 秒，具体保留哪些动作由实际生成效果决定。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。以下参考图用于人物、场景，不是固定首帧。
- 雨滴升起时近处伞面雨声短暂变薄，远处城市雨声持续；进入家中时窗边雨声渐渐融入。歌曲后期连续对齐，雨声建议后期分层处理。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰发色、发型和外出造型；多视图为同一人。
2. **图2 / Picture 2 — 乐正绫**：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。参考深红长发与人物外貌；水滴中的虚影面庞朦胧。
3. **图3 / Picture 3 — C 组家中回忆**：`MV/ab_test/C_anime_pbr/06_memory.png`。参考暖灰雨天的家、窗帘、雨窗和两只杯子。
4. **图4 / Picture 4 — 洛天依居家服**：`MV/pictures/Luo_Tianyi_Home_Turnaround_Side_Revision.png`。参考家中洛天依的米白开衫、浅蓝上衣和蓝灰长裙；多视图为同一人。

两个模型版本按同一顺序上传。透明伞和雨滴由提示词描述；两人的虚影只出现在水滴中，淡去后才显现家中的回忆画面。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, referenced from <Picture 1> for her appearance and rainy-street look and from <Picture 4> for her cream cardigan, pale blue top and blue-grey skirt in the home memory. Both pictures depict the same person.
<Subject 2> is Yuezheng Ling, referenced from <Picture 2> for her dark red hair and appearance; her face is indistinct in the raindrop vision.
<Subject 3> is the warm-grey home interior referenced from <Picture 3>, including its curtains, rain-streaked window and two cups.

summary:
[reference generation] A raindrop rises from <Subject 1>'s transparent umbrella and fills most of the frame. Hazy images of <Subject 1> and <Subject 2> appear within it and fade; <Subject 3> appears inside the drop, and the camera pushes forward into the home. The two sit by the rainy window and share a quiet glance.

retention_analysis:
<Subject 1> (appears in [Shot 1]): partially_preserved - Use her umbrella in the opening, a hazy image inside the drop, and her home outfit in the memory; do not reproduce either reference-sheet layout.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep her recognizable dark red hair while using a misty image in the drop and a natural figure in the home memory.
<Subject 3> (appears in [Shot 1]): partially_preserved - Retain the room, curtains, rainy window, two cups and warm-grey daylight, adapting the viewpoint for the transition.

detailed_description:
A semi-realistic Japanese anime film with PBR-like materials and clean, restrained detail. The present is a cool blue-grey rainy night; the home memory has soft warm-grey rainy daylight.
[Shot 1] Start in macro close-up on the edge of <Subject 1>'s transparent umbrella. Raindrops fall onto the canopy and slide along the clear rim. One droplet detaches and slowly rises while surrounding rain continues to fall downward. The camera follows and moves closer until the droplet fills most of the frame. Within it, misty side-by-side images of <Subject 1> and <Subject 2> gently fade in, linger briefly and fade away; their faces are indistinct. After the figures disappear, a soft image of <Subject 3> gradually appears inside the drop. The camera continues pushing forward into this image, revealing the rainy window, curtains and room as the frame becomes the home memory. By the window, <Subject 1>, now wearing her home cardigan, sits beside <Subject 2>. They quietly watch the rain, then exchange a gentle glance. Two cups sit on the nearby table. Hold on their interaction and the rain outside through the end. The droplet-to-home transition is visual; the drop does not physically flood the room.

overall_soundscape: The close umbrella-rain texture briefly thins as the drop rises, while distant city rain remains. Soft window rain gradually enters as the camera pushes into the home. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成从雨夜伞沿进入雨天家中回忆的 MV 片段。洛天依的外貌和雨夜造型参考图1、居家服参考图4，两张图是同一个人；乐正绫的外貌和深红长发参考图2；家中的雨窗、窗帘和室内参考图3。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头微距对准洛天依透明伞的边缘。雨滴落在伞面，水珠沿伞沿滑动；其中一颗脱离伞沿，缓缓向上升起，周围其他雨滴仍正常向下落。
2. 镜头跟随这颗雨滴向前靠近，水滴逐渐占据画面的大部分区域。水滴中柔和淡入洛天依与乐正绫并肩的朦胧身影；两人的面庞看不清，身影停留片刻后轻轻淡去。
3. 两人的虚影消失后，水滴中渐渐显现雨天家中的画面。镜头继续向前推入水滴里的画面，窗户、窗帘和室内逐渐清晰，进入暖灰色的家；窗外仍在下雨，雨痕沿玻璃向下流。
4. 家中，穿着针织开衫的洛天依与乐正绫靠窗坐在一起，先安静看雨，再互相看一眼。桌上放着两只杯子；画面在两人的互动中停留至片段结束，不急切回街道。

【音频风格】
雨滴升起时，近处伞面雨声短暂变薄，远处城市雨声保留；镜头进入家中时，窗边雨声渐渐融入。无对白，不另作配乐。

【运镜与核心约束】
伞沿微距跟随单颗雨滴，向前靠近至雨滴占据画面大部分区域；虚影淡去后，家中的画面在水滴内显现，镜头继续向前推入。只有一颗雨滴向上升起；虚影朦胧并柔和淡入淡出，进入家中后留出互动时间。
```

## 剪辑与衔接

- 一次生成完整 14 秒；前约 7 秒为升滴与虚影，后约 7 秒为家中显现、推入和互动。最终按歌曲与动作完成度剪辑，成片约 12 秒。
- 虚影消失后家中画面才显现；镜头继续向前推入，不做向后拉镜。家中是回忆，片尾停留在两人的互动。
- 若一次生成不能稳定完成多阶段转场，可拆成伞沿升滴、雨滴虚影、推入家中与互动等片段，按实际尾帧和镜头匹配情况后期组接。
- 镜头 13 的递热饮可从桌面和两只杯子接续；人物位置和取杯动作等本段生成后再确定。
- `output\shot10.mp4` 的尾帧是雨夜城市街道远景，可以切到伞沿微距并以雨声衔接；最终选用的剪辑点可能不同。
