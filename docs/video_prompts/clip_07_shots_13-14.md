# 片段 07｜递来的热饮与掌心水珠（剧本镜头 13–14）

## 片段信息

- 剧本成片区间：1:02–1:14；镜头 13 为 1:02–1:08，镜头 14 为 1:08–1:14。
- 建议设置：横屏 16:9，生成 **13 秒**；成片取约 12 秒，预留约 1 秒剪辑余量。前半段为家中递饮和站起，中间以水珠和蓝黑色完成连续场景变换，后半段停留在雨夜掌心与侧脸近景；实际节奏按生成结果和歌曲调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图片是人物和环境参考，不是固定首帧。
- 前段家中回忆为柔和暖灰白昼，后段现实街道为蓝灰雨夜。两人互动自然克制；片尾保留雨声供下一镜街边场景衔接。
- 歌曲后期连续对齐；杯底轻触桌面的声音与雨声可单独后期制作。剧本中的半侧面演唱为可选项，本版先保持闭口，不要求模型同步唱词。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依居家造型**：`MV/pictures/Luo_Tianyi_Home_Turnaround_Side_Revision.png`。参考银灰色低位马尾、花饰和米白针织开衫；多视图是同一人。
2. **图2 / Picture 2 — 乐正绫**：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。参考深红长发和深色衣服；她在家中向洛天依递饮，不在现实街道出现。
3. **图3 / Picture 3 — C 组家中场景**：`MV/ab_test/C_anime_pbr/06_memory.png`。参考窗边桌面、两只杯子、雨窗和暖灰日光；镜头从桌面近景切入。
4. **图4 / Picture 4 — 洛天依外出造型**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考雨夜中的灰色布料风衣、发型与透明伞下造型；图1和图4是同一位洛天依。

两个提示词版本使用同一上传顺序。前后人物与杯子的位置，以已生成的 11–12 实际尾帧为准：洛天依在画面左侧，乐正绫在右侧，两人窗边相对而坐，桌上有两只杯子。下述图片仅为参考，非逐帧延续；如所用模式支持固定首帧，可另取实际尾帧匹配或后期切镜。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, referenced from <Picture 1> for her appearance and cream cardigan at home, and from <Picture 4> for her grey fabric coat on the rainy street. Both pictures depict the same person.
<Subject 2> is Yuezheng Ling, referenced from <Picture 2> for her dark red hair and dark clothing.
<Subject 3> is the warm-grey home interior from <Picture 3>, including the window, table and two cups.

summary:
[reference generation] At <Subject 3>, <Subject 2> slides a warm drink toward <Subject 1>. <Subject 1> reaches for it, then stands. The home dissolves into water and a dark blue-black field while she remains in the same screen position; a rainy street gradually appears around her, and she looks at a drop in her palm.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): partially_preserved - Keep the same character, wearing her home cardigan in the memory and her grey coat outdoors; do not reproduce either reference-sheet layout.
<Subject 2> (appears in [Shot 1]): partially_preserved - Use her recognizable dark red hair and clothing in the home; her hand moves the cup, and she is absent from the street.
<Subject 3> (appears in [Shot 1]): partially_preserved - Keep the rainy window, table, two cups and soft daylight, adjusting the framing to a hand-and-cup close-up.

detailed_description:
A semi-realistic Japanese anime film with PBR-like materials and clean, restrained details. The home memory is soft warm-grey rainy daylight; the street is cool blue-grey rainy night.
[Shot 1] At <Subject 3>, <Subject 1> sits on the left and <Subject 2> on the right near the rain-streaked window. Two cups rest on the table. Frame their hands and the tabletop as <Subject 2> gently slides one warm drink toward <Subject 1>; the other cup stays on the table. <Subject 1> reaches toward the offered cup, then stands. The camera widens enough to keep her visible as she rises. Keep her in the same screen position through the transition: <Subject 2> gently fades while the home image blends into beads of water, and the surroundings darken to deep blue-black. <Subject 1> remains in place and visible; neither person turns into water. Fine falling rain and city lights gradually emerge around her from the darkness, revealing the rainy night street. Her home cardigan transitions into her grey outdoor coat as part of the memory-to-present visual transition, and a transparent umbrella appears above her. Now in the real street, she looks down at a small drop in her open palm. Move gently from her hand to her side face as she watches the water, thoughtful, lips closed. <Subject 2> is absent from the street. Hold the moment while rain continues to fall visibly beyond the umbrella.

overall_soundscape: Soft rain against the home window; a quiet cup-on-table sound. On the transition, city rain returns with a light umbrella patter; nearby rain remains gentle under the song. No dialogue.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成雨天家中回忆与雨夜街道相接的 MV 片段。洛天依的居家外貌和针织开衫参考图1、雨夜灰色风衣参考图4，两张图是同一个人；乐正绫的深红长发和衣着参考图2；家中雨窗、桌面及两只杯子参考图3。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头13：暖灰色雨天的家中，两人延续窗边相对而坐的状态：洛天依在左，乐正绫在右。镜头靠近桌面与双手，桌上有两只杯子；乐正绫轻轻把其中一杯热饮推向洛天依，另一只杯子留在桌上。
2. 洛天依伸手靠近杯子，随后站起。镜头稍微拉宽，始终保留她在画面中的位置；乐正绫轻轻淡去，家中环境的画面渐渐融入水珠，周围转为蓝黑色。洛天依留在画面原位，人物本身不消失或化成水。
3. 镜头14：雨丝和城市灯光从蓝黑色背景中逐渐显现，形成蓝灰色雨夜街道；洛天依仍在原来的画面位置，居家服随转场变成灰色风衣，头顶出现透明伞。她低头看向掌心的小水珠，镜头由手转到她的半侧脸近景。她安静地望着水珠，短暂怀念，乐正绫没有出现在现实街道。
4. 细雨持续落在伞外，伞面沾着水珠；画面在洛天依的神情上停留至结束。

【音频风格】
家中窗雨声柔和，杯子接触桌面有轻响；转到街道后，城市雨声和伞面雨声轻轻接续。无对白，不另作配乐。

【运镜与核心约束】
先用桌面和手部近景表现递杯，洛天依站起时拉宽画面；场景经水珠与蓝黑色连续渐变为街道，洛天依保持同一画面位置，再转到手与半侧脸近景。两只杯子和递杯方向保持清楚；家中是暖灰雨天，街道是蓝灰雨夜。此段不要求演唱口型。
```

## 剪辑与衔接

- 已检查 `output\shot11-12.mp4` 尾帧：洛天依居左、乐正绫居右，两人在窗边相对而坐，桌上两杯。可直接从两人镜头切到桌面和手部；该尾帧没有作为此提示词的固定首帧。
- 家中环境通过水珠和蓝黑色逐渐变成雨夜街景，洛天依保持画面位置；乐正绫随回忆画面柔和淡去，人物本身不化成水。服装和伞随转场切换为现实造型。
- 约第 7 秒完成由家中到雨夜的过渡，最终对齐 1:08；若站起、角色位置和换景难以一次稳定生成，可分别制作家中站起与街道站立素材，再以同位置匹配、叠化和水珠过渡组接。
- 14 结束于雨夜侧脸和雨声，可接下一段街边店招；“Rainie love”文字按最终唱句在后期加入。
