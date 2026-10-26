# No.41 出典の頁・番号・短い引用の照合

確認日：2026年10月26日。作者側の確認記録。

**選択した引用箇所の実在・頁・定理番号は一致した。文献全体の比較はPARTIAL、
歴史的新規性はINCONCLUSIVE。** 取得済みであることと、全頁を完全監査した
ことを区別する。同一の時間定理の既発表を確認したという意味ではない。

PDF頁はビューア上の1始まりの位置、誌面頁・本文頁は紙面に印刷された番号。
機械可読の位置、PDF全体のSHA-256、頁の抽出本文のSHA-256は
evidence/citation_checks.jsonに収録した。引用の改行と連続空白だけを正規化した。
第三者論文の全文・頁画像は同梱していない。

## 番号と頁の対応

| 資料 | 箇所 | PDF頁 | 誌面・本文頁 | 確認方法 |
| --- | --- | ---: | ---: | --- |
| Alameda–Dillman–Kenter 2024最終版 | Proposition 3.1 | 5 | 312 | 本文抽出＋描画目視 |
| 同最終版 | Theorem 3.3 | 6 | 313 | 本文抽出＋描画目視 |
| Alamedaほか arXiv:2008.06552v1 | Theorem 4.4 | 13 | 13 | 本文抽出＋描画目視 |
| Hogbenほか arXiv:1410.4191v1 | Remark 1.8 | 3 | 3 | 本文抽出＋描画目視 |
| Butler–Young 2013最終版 | §2開始・forcing chain容量 | 2 | 66 | 本文抽出＋描画目視 |
| 同最終版 | パスの蛇行配置・Figure 1 | 3 | 67 | 本文抽出＋描画目視 |
| 同最終版 | 重み付きTheorem 2 | 4 | 68 | 本文抽出＋描画目視 |
| Carlsonほか arXiv:1807.09404v1 | §6開始 | 17 | 17 | 本文抽出 |
| 同著者稿 | Theorem 7.1 | 19 | 19 | 本文抽出＋描画目視 |
| 同著者稿 | Lemma 7.2 | 19 | 19 | 本文抽出＋描画目視 |

AJC最終版では木のℓ=1の結果がProposition 3.2、一般のℓの引用がTheorem 3.3。
2019年Dillman–KenterのarXiv版で木がProposition 3.3であることと混同しない。
今回確認したのは2024年最終版の上の番号である。

## 短い引用と使用範囲

### S1_final

[確認したPDF](https://ajc.maths.uq.edu.au/pdf/88/ajc_v88_p308.pdf)。19頁。

* AJC_PATH：パスの最小1-leaky集合が両端であることを証明。No.41の時間式は記載した定理ではない。
  短い引用：「For the path on n vertices」。
* AJC_TREE：木の低次数頂点集合の定理を、2022年論文Theorem 4.4として引用。
  短い引用：「the optimal ℓ-leaky forcing set」。

PDF SHA-256：`01fe9fd1469573417fdfe8ea243cd2546ed08d78eba54de668a122da89372a06`。

### S2

[確認したPDF](https://arxiv.org/pdf/2008.06552v1)。21頁。

* RESILIENCE_TREE：ℓ=1のパスへの特殊化がK1。到達可能性の定理であり、時間式Aを直接記載したものではない。
  短い引用：「If T is a tree and B is the set of vertices in T」。

PDF SHA-256：`661259a4550ea26e1f8ac973aec047170a790363dca4272dc35e0f3214b05941`。

### S14

[確認したPDF](https://arxiv.org/pdf/1410.4191v1)。17頁。

* HOGBEN_BOUND：通常zero forcingのPT(G)<=|G|-Z(G)とその計数理由。固定leak・非最小初期集合への計数適用は作者側の補足。
  短い引用：「because at least one force must be performed at each time step」。

PDF SHA-256：`63cb5e2d5578b726e110867f2fecfcf32cba5d75ab6f04418849af1b55a7124e`。

### S10

[確認したPDF](https://ajc.maths.uq.edu.au/pdf/57/ajc_v57_p065.pdf)。7頁。

* BUTLER_CAPACITY：§2開始、forcing chainの容量 |S|(p(G;S)+1)>=n。
  短い引用：「Balancing the initial set with propagation time」。
* BUTLER_LAYOUT：パスの蛇行配置と通常throttlingの等号構成。
  短い引用：「Snaking a path into a box」。
* BUTLER_WEIGHTS：重み付き目的a|S|+b p(G;S)を扱う。No.41の根号式をそのまま掲載したものではない。
  短い引用：「relative costs of the initial set」。

PDF SHA-256：`f90ebd4876ae3bbcbde3cf326606a8b2b89cc6a6cb6df2fe151932be4586fe18`。

### S6

[確認したPDF](https://arxiv.org/pdf/1807.09404v1)。20頁。

* CARLSON_WEIGHTED：重み付きPSD throttlingの節。抽出本文で確認。
* CARLSON_CYCLE：通常zero forcingのcycle throttling。leak付き時間式の定理ではない。
  短い引用：「Standard throttling for cycles」。
* CARLSON_LEAF：通常throttlingで木の葉を除く不等式。同じPDF頁にある。

PDF SHA-256：`c27b4437b3ffe8563dd2651ab32ad311f75256d3601394685e29337f639d1f90`。

## 導出に使える範囲

K1は到達可能性の既知事実である。K2では既知の計数理由を用いるが、固定leakと
任意の初期集合への適用は再証明側で補足した。O1の時間保存、O2の片端leakの
厳密な数え上げも、今回の再証明側に置く。したがって「既知の時間定理を代入
すれば全て終了」とは扱わない。K3は既存の容量・最適化の位置づけを示す資料。

Carlsonらの確認箇所は通常／PSDのthrottlingを扱う。No.41の固定vertex leakと
同じ時間定理として流用しない。確認したのは20頁のarXiv著者稿であり、
最終刊行誌面との逐語比較を完了したという記録でもない。

## 取得と版の留意点

AJC、Butler–Young、Carlsonは先に取得していたPDFの同じバイトを再確認した。
AlamedaとHogbenのv1 PDFは今回公開URLから取得した。ウェブ取得系統ではAJCが
引き続きエラーになったが、保有している最終PDFを抽出・描画できた。アクセス
エラーと原文の不存在を同一視しない。

HogbenのarXiv登録は2014年だが、配信PDFの本文日付は2018年。2012年刊行版と
同じ本文だとは推定せず、今回確認したPDFのバイトと位置を固定した。

この確認は、今回の引用の取り違えという懸念を解消するためのもの。
文献の全定理・全参考文献・全最終版の網羅監査や、新規性の認証ではない。

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
