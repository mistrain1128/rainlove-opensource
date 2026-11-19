# 片段 08｜雨夜店面与车窗回忆（剧本镜头 15–16）

## 片段信息

- 剧本成片区间：1:14–1:27；镜头 15 为 1:14–1:20，镜头 16 为 1:20–1:27。
- 建议设置：横屏 16:9，生成 **14 秒**，成片取约 13 秒，预留约 1 秒剪辑余量。建议约 0:00–0:06.5 为街边店面，0:06.5–0:14 为公交车窗遮挡转入家中回忆；具体按歌曲和生成动作调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片作为造型与场景参考，不是固定首帧。实际生成如无法完成连续遮挡转场，可拆分公交驶过和家中两个素材后期衔接。
- 店招参考图已有“Rainie love”文字；招牌亮起与暖光可在生成时表现，但最终准确文字、显隐和唱句对齐由后期完成，不依赖模型正确拼字。
- 歌曲后期连续对齐。街道雨声逐渐恢复部分密度；公交驶过声过渡为家中柔和窗雨声。回忆结束后可在剪辑中用雨声接回街道，不要求本片段最后再生成一次切回。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰发色、低位马尾、花饰和灰色布料风衣；多视图是同一人。
2. **图2 / Picture 2 — C 组雨夜店面**：`MV/ab_test/C_anime_pbr/07_cafe.png`。参考街边店面、橱窗和暖灯；图中已有文字不作为生成阶段必须准确复现的内容。
3. **图3 / Picture 3 — C 组家中回忆**：`MV/ab_test/C_anime_pbr/06_memory.png`。参考暖灰白昼、雨窗、窗帘和桌上的两只杯子。
4. **图4 / Picture 4 — 洛天依居家造型**：`MV/pictures/Luo_Tianyi_Home_Turnaround_Side_Revision.png`。参考家中米白针织开衫、浅蓝上衣与蓝灰长裙；图1和图4是同一人。
5. **图5 / Picture 5 — 乐正绫**：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。仅供家中回忆里身旁人物的深红长发与轮廓参考；面庞不清晰、不作面部特写，她不出现在现实街道。

两个提示词版本按同一顺序上传。透明伞由提示词描述；家中另一个人物可以通过背影或局部轮廓表现，不额外增加人物。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, referenced from <Picture 1> for her grey coat and rainy-street appearance, and from <Picture 4> for her cream cardigan, pale blue top and blue-grey skirt at home. Both pictures depict the same person.
<Subject 2> is the rainy-night street-front cafe in <Picture 2>, with warm windows and a lit sign area; exact lettering is not required in the generated footage.
<Subject 3> is the warm-grey rainy-day home from <Picture 3>, with curtains, a rain-streaked window and two cups on the table.
<Subject 4> is Yuezheng Ling, referenced from <Picture 5> for her dark red hair and silhouette; in the home memory she is seen only from behind or as a partial indistinct figure.

summary:
[reference generation] Outside <Subject 2>, warm storefront light falls across <Subject 1>'s transparent umbrella. A passing bus window fills the view and visually transitions into the rainy window of <Subject 3>, where <Subject 1> sits beside <Subject 4> in a quiet memory.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one character, her grey coat in the street and her home cardigan indoors; do not reproduce the multi-view sheet layout.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep the cafe, window and warm lights; precise sign text is reserved for post-production.
<Subject 3> (appears in [Shot 2]): partially_preserved - Keep the rainy window, curtains, two cups and warm-grey daylight while adapting the camera position.
<Subject 4> (appears in [Shot 2]): partially_preserved - Suggest her dark red hair and silhouette from behind or partially out of frame, with no clear face; she is not physically present on the real street.

detailed_description:
A semi-realistic Japanese anime film with PBR-like glass and metal, clean surfaces and restrained reflections. The street is rainy blue-grey night; the home memory is a soft warm-grey rainy day. Rain falls visibly in exterior views, and there are only small shallow puddles.
[Shot 1] A medium view of <Subject 1> outside <Subject 2>. She wears her grey coat and holds an open transparent umbrella, still angled toward an empty space beside her. The cafe sign area and warm window lights brighten softly; the warm light reflects across the rain-dotted umbrella while fine rain continues to fall in front of the darker street. Hold her quiet profile and the storefront without requiring readable sign text.
[Shot 2] At 00:06.500, a bus moves naturally across the foreground of the rainy street. Its rain-streaked side window passes close to the camera until the glass fills the frame. Use the window as a visual wipe: its moving rain trails and reflected light blend into the stationary rain-streaked window of <Subject 3> in daylight, revealing the home interior. <Subject 1>, now in her home cardigan, sits near the window; two cups rest on the table. <Subject 4> is beside her, seen only from behind or partially at the edge of frame, with her face indistinct. They remain quiet while rain continues outside. Hold the home memory through the end, leaving an editable tail.

overall_soundscape: Continuous street rain and distant city traffic, with umbrella patter gradually regaining some presence. The passing bus and wet road are audible; as the window transition reveals the home, the exterior traffic recedes and soft window rain emerges. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜店面与雨天家中回忆相接的 MV 片段。洛天依的外出造型参考图1、居家造型参考图4，两张图是同一个人；雨夜店面参考图2，家中的雨窗、窗帘和两只杯子参考图3；家中身旁人物乐正绫的深红长发和轮廓参考图5。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头15：雨夜街边，洛天依身穿灰色风衣、撑着透明伞站在店面附近，伞仍偏向身旁空位。街边店面的暖光与招牌灯光渐渐亮起，暖色映在沾着雨珠的透明伞面；雨丝持续落下。店招最终文字留给后期添加。
2. 镜头16：一辆公交车从街道前景驶过，车窗上有向下流动的雨痕。车窗经过镜头并逐渐占满画面，雨痕和反光连到雨天家中静止的窗玻璃，完成从夜晚到白昼回忆的过渡。
3. 镜头进入柔和暖灰色的家中。洛天依换上针织开衫，靠窗坐着，桌上放着两只杯子；乐正绫坐在她身旁，以背影或局部轮廓出现，面容不清晰。窗外仍在下雨，两人安静停留至片段结束。

【音频风格】
街道雨声逐渐恢复部分密度，公交驶过声与湿路声掠过；画面进入家中后，车声退去、柔和的窗雨声融入。无对白，不另作配乐。

【运镜与核心约束】
从街边中景转到公交车窗遮挡画面，利用车窗雨痕衔接家中雨窗；街道雨丝持续可见，雨夜为蓝灰色，家中为暖灰白昼。乐正绫只出现在家中回忆里。店招准确文字后期添加。
```

## 剪辑与衔接

- 已检查 `output\shot13-14.mp4` 的尾帧：洛天依撑透明伞、画面为雨夜侧脸近景。15 从侧脸切至店面中景，伞与服装延续；实际使用的剪辑点不同，仍需核对人物朝向和伞的偏向。
- 约第 6.5 秒开始公交遮挡，车窗填满画面后接家中雨窗；声音在车驶过时从街雨平滑过渡到窗雨。公交与家中的机位不必物理相连，以遮挡剪辑实现时间跳转。
- 参考图的店招已经有英文文字，生成时可能继承或改变；要确保拼写和出现时机准确，可后期覆盖或替换，不把模型文字当作定稿。
- 若公交、车窗与家中一次生成不稳定，分别生成 15 店面、公交车窗遮挡、家中回忆，后期用占满画面的车窗叠化或遮挡切镜。最后可用雨声接 17 的伞下近景，不预设本片段已生成回到街道的画面。
- 镜头 18 已按用户意见移除乐正绫身影，只保留雨滴与城市仰拍。
