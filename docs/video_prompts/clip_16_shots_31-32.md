# 片段 16｜雨雾淡去，雨声回来（剧本镜头 31–32）

## 片段信息

- 剧本成片区间：2:53–3:07；镜头 31 为 2:53–3:00，镜头 32 为 3:00–3:07。
- 建议设置：横屏 16:9，生成 **15 秒**；成片取约 14 秒，预留约 1 秒剪辑余量。前约 7.5 秒为雨雾淡出与短暂家中回忆，后约 7.5 秒为洛天依的反应和落雨；实际按歌曲及画面调整。
- 模式：MiniMax H3 多图参考 Ref2VA；Wan 3.0 多图参考。图3为上一段实际尾帧，可供参考；当前提示词并未把它指定为固定首帧。若平台支持首帧控制，可在页面中另行指定，并检查上传编号。
- 乐正绫的身影从上一段**持续存在**，在本段 31 随雨雾柔和淡出，不再重新淡入。上一段尾帧给她生成了一把透明伞，本段将伞与身影一起柔和淡出，尽量维持素材连续。
- 近处伞面雨声在身影淡出时逐渐回来，之后完整雨幕继续；远处城市雨声始终存在。歌曲后期连续对齐，雨声建议后期分层制作和试听。

## 参考素材及上传顺序

1. **图1 / Picture 1 — 洛天依**：`MV/pictures/Luo_Tianyi_Outdoor_Turnaround_New.png`。参考银灰色低位马尾、花饰和灰色布料风衣；多视图为同一人。
2. **图2 / Picture 2 — 乐正绫**：`MV/pictures/Yuezheng_Ling_Front_Clear.png`。参考深红长发和深色外套；天桥身影的面容在雨雾中保持朦胧。
3. **图3 / Picture 3 — Shot 30 实际尾帧**：`MV/pictures/shot30_tail_reference.png`。从 `output\shot29-30.mp4` 提取；参考前景伸出的手、远处乐正绫及她的透明伞、雨雾和天桥视角。它只作为视觉参考，不保证逐帧连续。
4. **图4 / Picture 4 — 家中回忆**：`MV/pictures/C_anime_pbr/06_memory.png`。用于短暂闪回的暖灰白昼、雨窗和桌面；递杯的手由提示词描述。

两个模型版本按相同顺序上传。洛天依和乐正绫是不同角色；两人相距数米，伸出的手没有接触。天桥横跨道路，车辆在桥下；不要把先前不合格的桥面候选图当作已验证的几何参考。

## MiniMax H3｜Ref2VA

```text
subject_definitions:
<Subject 1> is Luo Tianyi, one person referenced from <Picture 1>, with silver-grey hair in a low ponytail, a flower accessory and an opaque grey fabric trench coat.
<Subject 2> is Yuezheng Ling, referenced from <Picture 2> for her dark red hair and dark coat; her face is softened by rain haze.
<Subject 3> is the preceding bridge image in <Picture 3>, showing <Subject 1>'s outstretched hand in the foreground and <Subject 2> farther away holding a transparent umbrella.
<Subject 4> is the warm-grey rainy-day home in <Picture 4>, including its rainy window and table.

summary:
[reference generation] Continue the emotional moment suggested by <Subject 3>: <Subject 2> and her umbrella gradually fade into the rain haze. A brief memory of a hand offering a warm drink at <Subject 4> interrupts, then the scene returns to <Subject 1>, who watches the rain without pursuing.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 3], [Shot 4]): partially_preserved - Keep one character's appearance and grey coat; use her foreground hand first, then her quiet reaction. Do not reproduce the character-sheet layout.
<Subject 2> (appears in [Shot 1]): partially_preserved - Keep the distant, mist-softened figure and the transparent umbrella visible in the prior frame, fading them out together; do not introduce her again after the fade.
<Subject 3> (appears in [Shot 1], [Shot 3], [Shot 4]): partially_preserved - Use the bridge-level perspective, rainy city and spatial relationship as visual guidance, not a locked first frame.
<Subject 4> (appears in [Shot 2]): partially_preserved - Use the warm-grey rainy-day home and table for a brief close-up, not the reference background as a fixed frame.

detailed_description:
A semi-realistic Japanese anime film with PBR-like materials and clean, restrained details. The bridge is a cool blue-grey rainy night; the brief home memory has soft warm-grey rainy daylight.
[Shot 1] Begin with a bridge-level view guided by <Subject 3>: <Subject 1>'s outstretched hand is in the foreground, and <Subject 2> stands several meters away under the transparent umbrella seen in the prior frame. Their hands remain apart. Wind stirs the rain and <Subject 2>'s dark red hair. Her mist-softened figure and umbrella slowly fade together into the rainy background; she does not turn into water or fragments. Fine rain keeps falling normally. The nearby umbrella patter begins to return gradually as she fades, while distant city rain continues.
[Shot 2] At 00:04.500, cut briefly to a memory close-up at <Subject 4>: a hand gently slides a warm cup across the table toward another hand. The rainy window is softly visible behind them. The image holds for a moment without requiring faces.
[Shot 3] At 00:06.500, cut back to the same rainy bridge. <Subject 2> and her umbrella are no longer there. <Subject 1>, holding her own transparent umbrella, remains in place and lowers her extended hand slightly; she does not follow. The nearer umbrella patter continues to return.
[Shot 4] At 00:07.500, cut to a quiet close view of <Subject 1>'s face as she watches the rain where the figure was. Her expression is restrained and her lips remain closed. A few drops fall to the bridge pavement, creating small ripples in a shallow patch of water. Rain remains visible through the end; the full near and distant rain ambience has gradually returned.

overall_soundscape: Distant city rain and traffic continue throughout. The nearby umbrella patter gradually returns during the fade; the brief home memory carries soft window rain and a light cup-on-table sound. The complete layered rain ambience returns after the memory. No dialogue or dramatic sting.

non_diegetic_music: N/A
```

## Wan 3.0｜结构化请求

```text
【核心任务】
生成一段 15 秒的雨夜天桥与短暂家中回忆 MV 片段。洛天依的外貌和灰色风衣参考图1；乐正绫的深红长发与深色外套参考图2；上一段天桥画面、前景伸出的手和远处身影参考图3；家中雨窗和桌面参考图4。画面采用半写实二次元、PBR 质感。

【情节概要】
1. 镜头1 0–4.5秒：延续图3的情绪与空间关系。洛天依伸出的手在前景，数米外乐正绫撑着透明伞站在雨雾里，两人的手没有接触。风轻轻吹动她的发梢；她和伞一起在朦胧雨雾中缓缓淡出，人物不化成水滴或碎片。
2. 镜头2 4.5–6.5秒：短暂切到暖灰色雨天的家中。桌面近景里，一只手轻轻把一杯热饮推向另一只手，雨窗在后方柔和虚化；不需要人物面部特写。
3. 镜头3 6.5–7.5秒：切回雨夜天桥。乐正绫及她的伞已经不在；洛天依撑着自己的透明伞留在原处，伸出的手轻轻放低，没有继续追赶。
4. 镜头4 7.5–12秒：切到洛天依的侧脸近景。她安静望着身影消失的方向，神情克制，嘴唇自然闭合；身后的雨和城市灯光仍然可见。
5. 镜头5 12–15秒：切到桥面近景，几滴雨落到局部浅水迹中，泛起细小涟漪。雨幕持续，镜头停留片刻，为下一段留出衔接。

【音频风格】
远处城市雨声和桥下车流声持续。乐正绫淡出时，近处伞面雨声逐渐回来；短暂回忆里有柔和窗雨和杯子接触桌面的轻响，回到天桥后完整雨幕逐渐恢复。无对白，不另作配乐。

【运镜与核心约束】
从天桥远近同框切到家中递杯近景，再切回天桥人物侧脸与落雨近景。乐正绫只在本段开头连续淡出，不重新出现、不化成雨滴；两人保持距离，不触碰。雨丝持续可见，洛天依保持自然撑伞，为后续放低伞的动作留空间。
```

## 剪辑与衔接

- 已检查 `output\shot29-30.mp4` 尾帧：洛天依伸出的手在前景，乐正绫在数米外，画面为雨雾中的天桥视角；生成结果给乐正绫加了透明伞。本段按实际尾帧让她与伞一起淡出，不将生成结果误记成没有伞。
- 图3仅作视觉参考。若用户实际选择不同剪辑点，应从选中的尾帧重新核对两人距离、手势和伞的位置；若模型难以稳定延续，可先单独生成淡出，再切入已有家中递杯素材。
- 建议约第 4.5 秒切到递杯回忆，6.5 秒回天桥，7.5 秒进入洛天依反应，12 秒切落雨；按 3:00 的歌曲位置与实际画面调整，预留约 1 秒。
- 身影不重新出现，也不化成雨滴；近处雨声在淡出时逐渐恢复，远处城市雨声保持。雨声变化需实际在后期铺设、试听，不能只靠文字描述。
- 片尾仍让洛天依撑伞，镜头 33 再完整表现她缓慢放低伞，雨落肩头。
