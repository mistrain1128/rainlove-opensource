# 09–10 插入镜头｜雨雾中的乐正绫

## 片段信息

- 用途：单独生成乐正绫的雨中身影，后期按需要插入 09–10；原有片段无需重新生成或修改。
- 推荐设置：横屏 16:9，生成 **5 秒**，后期截取需要的长度。具体插入点随现有画面与歌曲决定，不改变原剧本时间轴。
- 图1 / Picture 1：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。参考人物、深红长发和深色长外套；参考图面部清晰，成片中的面庞由雨雾和反光遮模糊。
- 图2 / Picture 2：`MV/ab_test/C_anime_pbr/03_bus_shelter.png`。参考公交站附近的雨夜街道、灯光与城市氛围；不要求复制构图。
- 不生成新的音乐；雨声可后期与原片段衔接。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Yuezheng Ling, referenced from <Picture 1> for her long dark red hair, hair accessories and dark long coat.
<Subject 2> is the rainy city street near the bus shelter, referenced from <Picture 2> for its setting and blue-grey night lighting.

summary:
[reference generation] In <Subject 2>, <Subject 1> gently fades into the rain haze, lingers briefly, then fades away.

retention_analysis:
<Subject 1> (appears in [Shot 1]): partially_preserved - Keep her hair and clothing recognizable, while the face shown clearly in the reference becomes indistinct in the target shot.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep the rainy street and lighting, using a different camera view.

detailed_description:
A semi-realistic Japanese anime city at rainy blue hour, with soft lights and fine rain visibly falling throughout.
[Shot 1] A steady medium-long view looks along <Subject 2>. <Subject 1> slowly fades into view through the rain haze beneath the streetlights. Her long dark red hair and dark coat remain faintly recognizable, while mist and soft reflected light obscure her face. She stands quietly for a moment, then gently fades back out into the haze. Rain continues to fall normally across the entire shot.

overall_soundscape: Continuous rain and distant city traffic. No dialogue or dramatic sound effect.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜街道的 MV 插入片段。乐正绫的外貌、深红长发和深色长外套参考图1；公交站附近的雨夜城市和灯光参考图2。画面采用半写实二次元、PBR 质感。

【情节概要】
乐正绫的身影在街灯下的雨雾中缓缓淡入，安静停留片刻，再轻轻淡出。她的头发和衣服隐约可辨，面庞被雨雾和反光模糊。

【音频风格】
雨声和远处城市声持续，无对白，不另作配乐。

【运镜与核心约束】
平稳的中远景，雨丝始终可见；身影的出现和消失使用柔和淡入淡出，带有朦胧雾感。
```

## 剪辑建议

- 以独立插入镜头使用，可按需要裁掉淡入或淡出的部分；与既有 09–10 画面通过切镜及连续雨声衔接。
- 参考图是清晰人物，面庞的朦胧由生成和后期控制；生成结果不理想时可后期降低清晰度及调整淡入淡出。
