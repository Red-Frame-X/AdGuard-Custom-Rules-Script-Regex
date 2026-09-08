# DNS Blocklist Guide

DNSブロックリストのガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260908 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSやDNSブロッカーが名前解決時に参照できる、`IPアドレス ホスト名`形式のレガシーなリストです。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPアドレスとホスト名を記述します。通常は記載したホスト名そのものを対象とし、サブドメインを自動的にワイルドカード扱いするかどうかは読み込む実装に依存します。
* **メリット**：形式が単純で、hosts形式を受け付けるOSやDNSブロッカー間で再利用しやすいです。親ドメインを配下ごと遮断しない実装では、意図しないサブドメインまで巻き込む過剰ブロックを避けやすい利点があります。
* **デメリット**：サブドメインを個別に列挙するリストではファイルが大きくなりやすく、ワイルドカードや例外ルールなどの高度な表現は標準的なhostsファイルそのものにはありません。

### ドメインのみ（Domains only）
IPアドレスやフィルタ修飾子を付けず、ブロック対象のドメインを1行に1件ずつ記述するシンプルな形式です。

* **挙動・特徴**： `example.com` や `ads.example.com` のようにドメイン名だけを記述します。親ドメインの指定時にサブドメインも対象となるかは、使用するDNSブロッカーの実装に依存します。
* **メリット**：構文が単純でファイルサイズを抑えやすく、多くのDNSブロッカーで読み込めます。IPアドレスを含むHosts形式より再利用しやすく、リストの変換や管理も容易です。
* **デメリット**：標準化された単純なdomains-onlyリスト自体には例外ルールや正規表現などの高度な制御を記述できません。また、サブドメインの扱いが製品ごとに異なるため、利用環境の仕様確認が必要です。親ドメインを配下ごと遮断する実装では、正常なサービスまで巻き込む過剰ブロックにも注意が必要です。

### Adblock-styleのDNSブロックリスト
AdGuard DNSなど一部のDNSフィルタリングエンジンは、Adblock系のネットワークルール構文の一部をDNSレイヤー向けに解釈できます。

* **挙動・特徴**：AdGuard DNS filtering syntaxでは、例えば `||example.com^` でドメインをブロックし、`@@||example.com^` で例外を作成できます。
* **メリット**：対応製品ではブロックと例外を同じルールセットで管理できます。
* **デメリット**：対応する解析エンジンが必要です。DNSフィルタが解釈できるのは製品が対応する構文だけであり、URLパス、リソース種別、DOM要素などDNS問い合わせから判断できないブラウザ向けルールをそのまま流用しても同じ結果にはなりません。

AdGuard公式のDNS filtering rules syntaxでは、Adblock-style、`/etc/hosts`、domains-onlyを区別しています。ブラウザ用フィルタを無変換でDNSへ投入すると、DNSレイヤーで意味を持たないルールや未対応modifierは期待どおりに動作しません。DNS用リストは「ブラウザ用フィルタの縮小版」ではなく、DNSで評価できる情報だけを使う別レイヤーのルールセットとして扱います。

---

## 2. AdGuard for Android / personalDNSfilter 向け候補

ここでは保守元、形式、利用環境との互換性を確認しやすい候補を1つずつ示します。「最適」は端末性能、必要なサービス、誤ブロックの許容度で変わるため、ログを確認しながら選択します。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング向けのリストです（AdGuard SDNSFilter）。

* **購読用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)

* **メリット**：AdGuard DNSフィルタリング向けに保守され、AdGuardのDNSフィルタ構文との互換性を確認しやすい候補です。
* **デメリット**：他製品が同じAdblock-style DNS構文を解釈するとは限りません。他社製アプリへ流用すると、一部のルールや例外が無視される可能性があるため、その製品が公式に受け付ける形式を優先します。

### HaGeZi's Normal DNS Blocklist（personalDNSfilter向け）
複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Normalは作者が「balanced protection」と位置付ける中間的な選択肢です。

* **購読用URL**：[HaGeZi's Normal DNS Blocklist（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)

* **メリット**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べます。
* **デメリット**：より強いリストほど対象範囲が広がり、アプリのログイン、通知、決済、CDNなどを巻き込む可能性も増えます。Normalを含め、実環境のログで誤ブロックを確認します。

---

## 3. アプリ別の構成例

### AdGuard for Androidの場合
まずは **「AdGuard DNS filter」** 単体から開始します。
* **メリット**：アプリとフィルタの保守元が同じで、構文差による問題を切り分けやすくなります。
* **デメリット**：AdGuard固有のDNSルール構文を含む場合、同じリストを他のDNSブロッカーへそのまま移行できるとは限りません。

### personalDNSfilterの場合
ダウンロードするブロックリストには、公式プロジェクトが想定するhostsまたはdomains-only系の単純な形式を使用します。このガイドでは **「HaGeZi's Normal DNS Blocklist（Domains only）」** を単体で指定します。

personalDNSfilterの`additionalHosts.txt`は、ダウンロードするリストとは別のローカル上書き機能です。公開されている標準ファイルでは、1行1ホストのブラックリスト、`!`接頭辞のホワイトリスト、`*`ワイルドカード、`>`によるカスタムIPマッピングが定義されています。これはAdblock Plusの `||example.com^` / `@@||example.com^` 構文とは別物です。

* **メリット**：ダウンロードリストを単純な形式に保ちつつ、必要な例外やローカル指定を`additionalHosts.txt`側で追加できます。
* **デメリット**：AdGuard DNSのAdblock-style構文をそのまま移植することはできません。また、親ドメイン・サブドメインやワイルドカードの優先順位はpersonalDNSfilterの実装に従います。

---

## 4. ブラウザ用コンテンツブロッカーとの併用

ブラウザ用コンテンツブロッカーとDNSブロックは、同じものを二重に動かす構成ではありません。DNSは名前解決段階、uBlock OriginやAdGuard Browser Extension等はブラウザ内のリクエスト・DOM・スクリプトレット等を扱います。

### 併用の利点

* ブラウザ外のアプリ通信にもDNSレベルの遮断を適用できる
* 既知の広告・トラッキングドメインを名前解決段階で遮断できる
* ブラウザ側はURLパス、リソース種別、要素隠蔽、スクリプトレット等の細かい処理に集中できる

### 併用の欠点

* DNSで先に遮断された通信はブラウザ側Loggerだけでは原因を追跡できない場合がある
* 同じサービスを両レイヤーで例外化しないと復旧できないことがある
* 強いDNSリストを追加しすぎると、アプリのログイン、通知、決済、CDN等まで巻き込む可能性がある

### トラブルシューティング

誤ブロックやアンチ広告ブロックを調査するときは、構成を一時的に単純化します。

1. ブラウザ用ブロッカーを1つに絞る
2. 追加フィルタを最小構成へ戻す
3. DNSブロックを一時的に外して再現性を確認する
4. ブラウザ側Logger / AdGuard Filtering logとDNS側ログを別々に確認する
5. 原因レイヤーが分かった後に最小の例外ルールを作成する

uBlock Origin公式は、uBOと別のブラウザ用コンテンツブロッカーの併用を非推奨としています。一方、DNSブロックは別レイヤーなので併用自体は可能ですが、切り分け可能な構成にしておくことが重要です。

---

## ソース・参考文献

仕様の確認には、各プロジェクトの公開資料を優先します。

**形式と構文**
* [AdGuard DNS filtering rules syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/)
* [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
* [personalDNSfilter `additionalHosts.txt`](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/assets/additionalHosts.txt)
* [personalDNSfilter](https://github.com/IngoZenz/personaldnsfilter)
* [uBlock Origin README — 他のコンテンツブロッカーとの併用について](https://github.com/gorhill/uBlock/blob/master/README.md)

**フィルタの公式リポジトリ**
* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
