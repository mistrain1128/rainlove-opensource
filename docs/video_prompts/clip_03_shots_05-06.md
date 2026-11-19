# 片段 03｜雨夜里的习惯：人行道与便利店（剧本镜头 05–06）

## 片段信息

- 剧本成片区间：0:15–0:25；镜头 05 为 0:15–0:20，镜头 06 为 0:20–0:25。
- 推荐页面设置：横屏 16:9，生成时长 **12 秒**。建议片段内 0:00–0:06 为镜头 05，0:06–0:12 为镜头 06；最终各取约 5 秒，共约 2 秒剪辑余量。根据实际动作完成度和最终混音调整剪辑点。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。参考图限定人物与环境，不是固定首帧。
- 歌曲作为整支 MV 的主音轨在后期对齐；生成的雨声与隔玻璃店内声可作为参考或由后期单独铺设。无对白，不另作配乐。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo Tianyi.png`。参考银灰色单侧马尾、蓝色眼睛、花饰和不透明灰色布料风衣；多个视角为同一个人，不将角色设定图版面带入画面。
2. **图2 / Picture 2 — C 组便利店街道**：`MV/ab_test/C_anime_pbr/02_convenience.png`。参考暖光玻璃店面、雨夜人行道、城市街景和半写实二次元材质；店内人物由提示词生成，视角按分镜调整。

两个提示词版本使用同一上传顺序。图1仅用于洛天依；路人和店内顾客是普通背景人物，不复制洛天依的造型。透明伞延续前一段，伞下空位没有人。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person whose appearance comes from <Picture 1>: silver-grey side ponytail, blue eyes, flower hair accessory and an opaque light-grey fabric trench coat.
<Subject 2> is the rainy Japanese urban sidewalk and convenience store from <Picture 2>, with warm light behind the glass, wet paving and a cool blue-grey street.

summary:
[reference generation] <Subject 1> walks along <Subject 2> with her transparent umbrella tilted toward an empty space, then notices a customer handing a warm drink to a companion inside the convenience store and looks away.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep one Luo Tianyi and her outfit and hairstyle; do not reproduce the character sheet layout.
<Subject 2> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the same convenience-store frontage, warm glass and rainy sidewalk while changing camera position; add ordinary pedestrians and customers to the otherwise empty reference.

detailed_description:
A semi-realistic Japanese anime city at rainy blue hour with PBR-like glass and metal, clean surfaces, restrained reflections and a few small shallow puddles. Rain is visibly falling throughout both shots: distinct, fine rain streaks descend through the foreground and background, clearly illuminated against the dark street and warm storefront light. The rain is continuous, not merely a wet-ground look. The warm convenience-store light contrasts softly with the cool wet street.
[Shot 1] A medium view follows <Subject 1> slowly along the sidewalk beside <Subject 2> as visible rain falls steadily around her. Raindrops strike her open transparent umbrella and bead and run down its canopy; scattered drops strike the pavement and form small ripples in shallow puddles. She wears her grey fabric trench coat. The umbrella remains tilted toward an empty space at her side, leaving the opposite shoulder exposed to the falling rain. She passes ordinary pedestrians and subtly tightens her hand around the umbrella handle while continuing forward. The background pedestrians move naturally past her; none shares her umbrella. Keep her appearance, the umbrella and her direction of travel consistent as the camera follows.
[Shot 2] At 00:06.000, cut to a side view of the same convenience-store window. Rain continues visibly falling outside, with fine streaks passing in front of the warm window; fresh droplets strike the glass and merge into narrow trails running down it. <Subject 1> is outside beneath the umbrella, which continues to catch the rain. Inside the store, one ordinary customer hands a warm drink to their companion. The two customers remain behind the glass, separate from her. She notices the exchange, pauses briefly and then turns her gaze away. The empty space beneath her tilted umbrella remains unoccupied. Let the final gaze settle briefly before the clip ends, with rain still visibly falling.

overall_soundscape: Continuous rain on the umbrella and pavement, subdued distant traffic and footsteps. Store sounds are faint and muffled through the glass. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨夜人行道与便利店的 MV 片段。洛天依的外貌、银灰色单侧马尾、花饰和灰色布料风衣参考图1；图中的多个视角共同指向同一个人。便利店玻璃橱窗、暖光、湿润人行道和城市街景参考图2。画面采用半写实二次元和 PBR 质感。

【情节概要】
1. 镜头05：洛天依撑着透明伞走过人行道上的行人，握紧伞柄；伞仍偏向身旁空位，自己的另一侧肩膀露在雨里。
2. 镜头06：切到便利店橱窗侧景。暖光透过雨珠，她从店外看见店内一位顾客向同伴递热饮；她停顿后移开视线。店内两人留在玻璃另一侧，伞下空位没有人。

【音频风格】
雨声、脚步与远处车辆声延续；店内声音隔着玻璃模糊。无对白，不另作配乐，歌曲在后期与全片对齐。

【运镜与核心约束】
镜头05以中景缓慢跟拍，镜头06切到橱窗侧景。两镜保持洛天依、透明伞及其偏向一致；路人和顾客是普通背景人物。地面湿润，水洼小而局部，反光克制。
```

## 剪辑与衔接

- 镜头 04 以背影走向街道结束，镜头 05 接续行走；实际生成后核对人物行进方向、伞的偏向、露出的肩膀和光线。此前片段尾帧尚未确认，不将其视作已锁定的首帧。
- 镜头 05 与 06 使用同一张便利店参考图：先在店外人行道跟拍，再切至同一店面橱窗侧景；生成后检查门窗、街道方向是否足够一致。
- 片内约第 6 秒切镜，最终按动作完成度各取约 5 秒。若模型难以同时稳定表现行走、切镜与店内递饮，可拆开生成镜头 05 和 06，再单独剪辑；届时仍需检查人物、伞和店面连续性。
- 镜头 06 的收尾是移开视线，镜头 07 将转入手与屋檐滴水的近景；后续以切镜衔接，不预设模型会生成连续尾帧。
