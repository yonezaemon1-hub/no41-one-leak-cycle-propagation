> Archive note added for v0.2: this is the detailed source review completed
> before receiving the supplied audit. Statements about an audit not yet received
> describe that earlier snapshot; see AUDIT_INTEGRATION_JA.md for current status.
> It is not a new run or a historical-novelty certificate.

# No.41 新規性調査 - 2026年10月26日

対象：*Exact Parallel Propagation and Throttling with One Leak on a Cycle*, v0.1。

**結論：照合した原文では、配置ごとの最悪時間の同一定理は未発見。
歴史的新規性は INCONCLUSIVE。根号式と最適化の計算は、独立の新規成果として数えない。**

本記録は作者側の文献調査・数理的対応の分析であり、外部の独立監査ではない。
数学本文や既存の有限検証を変更する報告ではない。公開は HOLD のまま。

## 1. 新規性の候補を絞り直す

| 主張 | 今回の整理 |
| --- | --- |
| vertex-leaky zero forcing という故障モデル | 既知。新規性の対象外 |
| サイクルの最小1-leaky配置数が2 | 既知。新規性の対象外 |
| 初期配置数と伝播時間の和を最小化する問題設定 | throttlingとして既知 |
| 定理A：任意の初期配置 B の最悪時間を、長い青連続部分の間の白総数の最大値で表す | 同一記述は今回未発見。新規性を検討する中心 |
| 定理B：固定配置数 k に対する最適時間 | 定理Aと均等配置から得る帰結。既知のパスの容量最適化との対応あり |
| 締切別の最小配置数 | 定理Bの初等的な反転。別の新規成果に数えない |
| 定理C：ceil(sqrt(8n))-2 | 既知のパスの最適化と同じ計算に帰着する。独立の最適化原理・根号則とは主張しない |

残す候補は「この故障モデルのサイクルで、任意の配置の時間を正確に数え、
既知の容量最適化へ還元できること」。leaky forcing、throttling、均等割当、
平方根型の最適化そのものを発明したという主張はしない。

## 2. 既知のパスの結果との具体的な対応

Butler–Young (2013), §2, pp.66–68 は通常の zero forcing について、
初期配置 s 点・並列時間 p の容量制約 n <= s(p+1) と、パス上の蛇行配置を扱う。
その重み付きの考え方も同論文にある。[R1]

以下の重み2の閉形式とNo.41への対応は、今回こちらで導出したもの。
原文にNo.41の根号式がそのまま掲載されていた、という報告ではない。

通常のパス P_N に s 点を配置する最適時間を a(N,s) と書くと、容量制約と
パスの配置構成から

    a(N,s) = ceil(N/s) - 1,   1 <= s <= N.

No.41の定理Bの式は、r>=1 に対して

    tau(n,2r)   = a(n,r) - 1,
    tau(n,2r+1) = a(n-1,r) - 1

という値になる（それぞれの配置数がn以下の範囲。全点初期青の0段も一致）。
たとえば偶数配置数では、n <= r(t+2) は、パスの時間を p=t+1 とした
n <= r(p+1) と同じ不等式である。

初期配置の重みを2にしたパスの最適値を

    Q(n) = min_S { 2|S| + pt(P_n,S) }

と置く。既知の容量と構成を使った整数最適化は

    Q(n) = min_r { 2r + ceil(n/r) - 1 }
         = ceil(sqrt(8n)) - 1.

整数コスト c で収容できる最大頂点数は

    max_r r(c+1-2r) = floor((c+1)^2/8)

となるので、丸めまで含めて上の閉形式を得る。

No.41の奇数配置数のコストと、1点少ない偶数配置数のコストとの差は

    1 + ceil((n-1)/r) - ceil(n/r)

で、0または1。したがって奇数配置数が和の最小値を厳密に改善することはない。
n>=3ではQの最適解をr<=floor(n/2)から選べるため、No.41の定理A/Bを
成立させる対応の下で

    th_1(C_n) = Q(n) - 1 = ceil(sqrt(8n)) - 2.

これは、根号式の計算を新しい最適化結果として数えるべきでない根拠になる。
一方、この数値対応だけでは、サイクルの故障下の動作とパスの動作の間の
対応は証明されない。その対応を担うのが候補の定理Aと配置構成である。
No.41全体が既知の直接帰結だと確定した、という判定にはしない。

## 3. 既知の証明との距離

Alameda–Dillman–Kenter (2024), §3.3, Proposition 3.4, p.313 は、
隣接2点を初期青にし、片側が漏れで止まっても反対側から進む議論を示す。[R2]

No.41はこの二方向の発想を利用している。したがって「新しい故障回避原理」
「新しい伝播機構」は主張できない。特にk=2の最悪時間n-2は、この既知の
構成の時間を数えれば得られる特殊例として扱う。

今回同一記述を見つけられなかった部分は、隣接青が複数箇所にあり、
その間に孤立した初期青も含む任意のBに対して、白の総数だけで最悪時間を
表す一般の配置別公式である。証明は小さく、既知の議論の精密化に近い。
独立監査では「別の時間付き定理の直接適用で済むか」を優先的に確認する。

## 4. 別名・同値モデルを除外しない

### edge-leaky / specified-leaky forcing

一般化された漏れの研究では、vertex、edge、指定された方向のforceの
禁止について、到達可能性の同値性が既にある。[R3]

No.41のサイクルについては、時間に関しても補足できる。辺を削除せず、
その辺を横切るforceだけを禁止する1-edge-leakを考える。定理Aの各区間で、
辺の禁止が片方の前線を止めても、反対側から白W_i点をW_i段以内に埋められる。
最大区間の青・白境界の辺を止めれば、他方から白を一つずつ進む必要があり、
W_i段が必要になる。初期青・青の辺の禁止は影響しない。初期に隣接青がない
配置は、forceの禁止だけでは動き出さない。

従って、このサイクルの配置別最悪時間はvertex版とedge版で同じになる。
指定方向の1-forceの禁止でも同じ区間議論が使える。これは今回の作者側の
補助導出で、既存の一般到達可能性定理を、時間定理として引用したものではない。
edge-leaky / specified-leaky の時間の先行結果も、同値な候補として調査対象に含めた。

### 初期配置の消失・頂点や辺の削除

Brownらのfault tolerant zero forcingは初期配置の一部を失うモデル。
v1の§5はその最悪伝播時間を扱い、v4の導入でもleakとの違いを説明している。[R4]
既存v0.1のC6対照では、隣接2点の一方からforceを禁止すると4段で完了し、
一方の初期青を消すと停止する。モデルを同一視できない。

また、edge-leakは辺を残してforceだけを禁止する。実際に辺を削除して
近傍数も変える操作とは異なる。削除版の結果を流用する場合も、時間を保つ
明示的な対応が必要になる。

### PSD forcing・距離による配置

通常のサイクルのthrottlingはCarlsonらのTheorem 7.1で既知であり、
PSD版・重み付きPSD版も同論文の対象である。[R5]
Eliasらはleaky PSDを定義し、サイクルなどの最小配置数を扱う。[R6]

PSDでは別々の白連結成分に対して、孤立した青が伝播を開始できる。
No.41の通常ルールではそれができない。単純な距離や最大の白連続長への
置換は、既存のC5例B={0,1,3}で失敗する。個々の白連続長は1だが最悪時間は2。
ただし、適切な圧縮・重み付き還元によって既知結果から導ける可能性は残る。

## 5. 今回の原文確認範囲

| 文献 | 確認した箇所・位置づけ |
| --- | --- |
| [R1] Butler–Young (2013) | 雑誌PDF全7頁を取得。§2の容量制約・パス配置・重み付き議論を確認。根号式との対応の基礎 |
| [R2] Alameda–Dillman–Kenter (2024) | 雑誌PDF全19頁を取得。定義、Proposition 3.4と証明、結語を確認。前回未取得だった最終版を追加 |
| [R3] Generalizations of leaky forcing | arXiv著者稿と博士論文第3章の同値性を確認。2023年雑誌最終PDFはHTTP 500で未確認 |
| [R4] Brownら (2025/2026) | v1の時間の定義・サイクル節、v4の故障モデルの説明。初期配置消失モデル |
| [R5] Carlsonら (2018著者稿、2019刊行) | 20頁の著者稿を取得。§6、Theorem 7.1、Lemma 7.2を確認。最終誌面との逐語比較は未実施 |
| [R6] Eliasら (arXiv v2、2024) | 16頁の著者稿の定義・グラフ族・結語。2025年刊行版との逐語比較は未実施 |
| [R7] Alameda博士論文 (2021) | 89頁PDFを取得。全文語句検索、目次、関連する第2・3章の定理・結語、第6章を確認 |
| [R8] Abbas (2024受理著者版、2025刊行) | 12頁PDFを取得。故障モデル同値性、§V・VI、結語を確認。制御可能性・leader選択が中心 |
| [R9] Bjorkmanら (2025) | 定義・既知のcycle値・主結果の範囲を確認。最小個数の研究 |
| [R10] Frijio (2026年9月) | 原文HTMLの主定理と範囲を確認。PSDのedge-editに対する最小個数の変動が中心 |
| [R11] Wang (2026年5月) | 著者公開稿の対象グラフと§7項目3を確認。別のグラフ族で時間・throttlingを今後の課題としている |

原文を取得したことと、全頁の全定理を逐語監査したことは区別する。
博士論文は前回の取得不能を解消できた。リポジトリの新しいDownloadリンクは
取得できなかったが、元の公開bitstreamから本文を取得した。

今回の調査は主に上記の文献と、その参考文献・別名の照合。商用の網羅的な
引用データベース検索や、全ての学位論文・最終刊行版の完全比較ではない。

## 6. 検索記録と限界

検索日：2026-10-26。二つの検索系統を使用。主な検索語は以下。

* leaky forcing / leaky zero forcing + propagation time / parallel / deadline / latency
* leaky throttling / one-leaky throttling / time-optimal
* edge-leaky forcing + propagation time / throttling
* specified leaks + propagation time
* fault tolerant zero forcing + propagation time / throttling
* total forcing + throttling / paired distance domination + cycle
* 根号式・floorを含む文字列とforcing/throttlingの組合せ

検索は一般のrate limiting、音響のleaky wave、通信のzero-forcingなどの
無関係な結果も返した。それらは根拠にしていない。検索で同じ式が出ないことは
未発見の証明にしない。集約サイトの要約は文献を探す手がかりとしてのみ使用した。

新規性の判定を変えた根拠は、検索件数ではなく、[R1]との具体的な式の対応と、
既知の漏れモデル・二方向伝播の証明との切り分けである。

## 7. 現在の判定と次の監査対象

| 項目 | 判定 |
| --- | --- |
| 同一の配置別時間定理 | 今回の確認範囲では未発見 |
| モデル・throttlingの新規性 | 主張対象外・既知 |
| 根号式を計算する最適化 | 既知の容量最適化に還元。独立した新規主張から外す |
| 故障下の動作から容量式への対応 | 候補として残る。独立確認未了 |
| 歴史的新規性 | INCONCLUSIVE |
| 文献比較 | PARTIAL・前回より改善 |
| 外部独立監査・人間の査読 | 未実施 |
| 数学・有限計算 | v0.1から変更なし。再実験は行っていない |
| 公開 | HOLD |

外部監査は次の一点を中心にする：

> 任意の初期配置Bについて、孤立した初期青をまたぐ白の総数が最悪時間に
> 一致する、という時間保存の還元が既にあるか。あるなら、定理番号・仮定・
> 写像を示してNo.41定理Aを導いてほしい。

この先行結果が見つかれば、定理BとCも帰結になるため候補全体の位置づけを
見直す。見つからない場合でも、「著者の確認範囲では同一結果を確認できなかった」
までに留め、世界初・歴史的優先権・人間の査読済みとは書かない。

## 8. 文献リンク

* [R1] Steve Butler and Michael Young, *Throttling zero forcing propagation speed on graphs*, Australasian Journal of Combinatorics 57 (2013), 65–71. [雑誌PDF](https://ajc.maths.uq.edu.au/pdf/57/ajc_v57_p065.pdf)
* [R2] Joseph S. Alameda, Shannon Dillman and Franklin Kenter, *Leaky forcing: a new variation of zero forcing*, AJC 88(3) (2024), 308–326. [雑誌PDF](https://ajc.maths.uq.edu.au/pdf/88/ajc_v88_p308.pdf)
* [R3] Joseph S. Alameda, Jürgen Kritschgau and Michael Young, *Generalizations of leaky forcing*. [arXiv:2009.07073](https://arxiv.org/abs/2009.07073); Journal of Combinatorics 14(4) (2023), 407–424, DOI [10.4310/JOC.2023.v14.n4.a1](https://doi.org/10.4310/JOC.2023.v14.n4.a1).
* [R4] Asher Brownほか, *Fault Tolerant Zero Forcing* / *Vertex Fault Tolerant Zero Forcing*. [v1](https://arxiv.org/html/2509.07854v1), [v4](https://arxiv.org/html/2509.07854v4).
* [R5] Joshua Carlsonほか, *Throttling positive semidefinite zero forcing propagation time on graphs*. [arXiv:1807.09404](https://arxiv.org/abs/1807.09404); Discrete Applied Mathematics 254 (2019), 33–46, DOI [10.1016/j.dam.2018.06.017](https://doi.org/10.1016/j.dam.2018.06.017).
* [R6] Olivia Eliasほか, *Leaky positive semidefinite forcing on graphs*. [arXiv:2312.10154v2](https://arxiv.org/abs/2312.10154v2); Involve 18(4) (2025), 719–735, DOI [10.2140/involve.2025.18.719](https://doi.org/10.2140/involve.2025.18.719).
* [R7] Joseph Stephen Alameda, *Variations of zero forcing and power domination*, Iowa State University dissertation (2021). [大学の登録ページ](https://dr.lib.iastate.edu/handle/20.500.12876/NveoRqOz), [取得できた公開PDF](https://dr.lib.iastate.edu/bitstreams/28143f00-c8d8-425e-b804-30c9515f256e/download).
* [R8] Waseem Abbas, *Leaky Forcing in Graphs for Resilient Controllability in Networks*, IEEE TCNS 12(1) (2025), 190–201, DOI [10.1109/TCNS.2024.3457582](https://doi.org/10.1109/TCNS.2024.3457582). [12頁の受理著者版](https://nebula.wsimg.com/d5a821f19bfaa9b030f79462cd457d3c?AccessKeyId=DC23973FEA94075ABCF3&alloworigin=1&disposition=0)、[先行するACC 2023著者稿](https://arxiv.org/abs/2303.02366)。取得した12頁PDFは2024年受理著者版であり、8頁の会議稿とは区別した。
* [R9] Beth Bjorkmanほか, *Leaky Forcing: Extending Zero Forcing Results to a Fault-Tolerant Setting*. [arXiv:2508.02564v1](https://arxiv.org/html/2508.02564v1).
* [R10] Domenico Frijio, *Sharp Edge-Edit Bounds at Every Level for Leaky Positive Semidefinite Forcing*. [arXiv:2609.22804v1](https://arxiv.org/html/2609.22804).
* [R11] Xinjun Wang, *Leaky Forts and l-Leaky Forcing in Common t-Clique Unions of Complete Graphs* (May 2026). DOI [10.5281/zenodo.20378616](https://doi.org/10.5281/zenodo.20378616), [著者公開稿](https://www.researchgate.net/publication/405320126_Leaky_Forts_and_l-Leaky_Forcing_in_Common_t-Clique_Unions_of_Complete_Graphs).

## 9. 取得資料の識別情報

以下は今回取得したPDFのバイト識別情報。第三者のPDFそのものは本記録に
同梱・再配布しない。本文の取得不能と版の差を、将来の監査で区別するために残す。

| 資料 | 頁数 | bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Butler–Young 雑誌版 | 7 | 104569 | f90ebd4876ae3bbcbde3cf326606a8b2b89cc6a6cb6df2fe151932be4586fe18 |
| Alameda–Dillman–Kenter 雑誌版 | 19 | 385239 | 01fe9fd1469573417fdfe8ea243cd2546ed08d78eba54de668a122da89372a06 |
| Alameda博士論文 | 89 | 618394 | dd34cc8f826315d23f1ef65acec5373fb779cd0748a40a04ccbc862fe85bef76 |
| Carlsonら arXiv著者稿 | 20 | 329805 | c27b4437b3ffe8563dd2651ab32ad311f75256d3601394685e29337f639d1f90 |
| Abbas 受理著者版 | 12 | 1856513 | 015e82f8ae709bc592404786839c0350885c2277c61173132169fdc69bc24dad |

対象v0.1 ZIPのSHA-256：
`69050b95e0249526f66111c8f035e2e3531d86ed144c10781c5eb12e5c605f62`。
そのZIPは変更していない。既存の1,966,072通りの有限計算を今回の文献調査で
再実行したとは主張せず、件数も追加していない。

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
