# ChromeOS & Android Optimization Guide

ChromeOS & Android 最適化ガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260908 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## Subscription
一部のサブスクリプションでは月額プランより割安な年額プランが用意されていますが、割引率、途中解約、払い戻しの条件はサービスごとに異なります。契約前に公式の料金ページと解約・返金条件を個別に確認します。

**利用中のサブスクリプション一覧**

サブスクリプションの購読基準は、「ITインフラになり得ているか」と「保守の負担比率が、対処 > 利用になった」という点に尽きます。

* Amazon Prime（年額）
* ChMate スタンダードプラン（月額）
* ChatGPT Plus（月額）
* Google AI Plus 400 GB（年額）
* [mond｜Kdroidwinさんのメンバーシップ](https://mond.how/ja/kdroidwin)（Premium / 月額）
* 𝕏プレミアム ベーシック（年額）
* YouTube Premium（年額）

トラブルを完全に避けるのであれば、サブスクリプションを一切契約しないのが最も安全です。
必要があって契約する場合は、トラブルの原因となりやすい携帯キャリア提供の月額オプションは避け、公式サイトが直接提供するプランを必要最小限選ぶのが無難です。

* **参考**： [【お詫び/復旧】一部お客さまでドコモからご契約いただいたYouTube Premiumがご利用いただけない事象について](https://www.docomo.ne.jp/info/notice/page/251222_03_m.html)

**Google One メンバーシップ・不具合**

下記の購入特典と有料プランにおいて、システム上で重複適用できてしまう不具合がありました。

1. Chromebook Plusの購入特典（Google AI Pro 2 TB 1年間無料）
2. docomo 爆アゲ セレクション Google One ベーシック（100 GB）（月額）
3. Google AI Pro 2 TB（年額）

確認を怠ってこれらを重複適用してしまうと、Google OneのWebサイトでストレージ容量を正確に取得できず、コンテンツの確認ができなくなるエラーが発生します。
* [エラー画像 1](https://imgur.com/CNjeA2d)
* [エラー画像 2（500エラー）](https://imgur.com/cIa8AJt)
* [エラー画像 3（Androidアプリ ロック状態）](https://imgur.com/a/u9f38dX#3dKWbMC)

> **※ 以下2つの記述は未検証の仮説です**
> 1. Google One メンバーシップ プランの管理権限が、Googleからdocomoの月額プランへ一時的に移管されます。
> 2. dポイントが付与される代わりに、Google公式のAIプラン（Google AI Plus 200 GB〜）が選択できなくなります。（[参考URL](https://one.google.com/about/plans?hl=ja-JP&g1_landing_page=0)）

不具合の内容をコピー＆ペーストできるようメモにまとめ、お問い合わせ方法からチャットを選択します。
* **[Google One ヘルプ > お問い合わせ](https://support.google.com/googleone/gethelp)**

docomo経由で契約したサービスの問い合わせ先やサポート範囲は、契約内容と窓口によって異なります。ahamoを含め、一律にサポート不可とは判断せず、対象サービスの公式窓口案内を確認します。
* **[docomo｜ご意見・ご要望](https://www.docomo.ne.jp/support/inquiry/feedback/?hl=ja-JP)** > 「ご意見・ご要望はこちら 開く+」をクリックする。

過去に同様の不具合がなかったかRedditで検索したところ、既存の有料プランにGoogle Pixelの購入特典を重複適用した結果、Google One メンバーシップに問題が発生したという報告も見つかりました。

* **[Google free trial Premium AI Scam](https://www.reddit.com/r/GoogleOne/comments/1dqzsrv/google_free_trial_premium_ai_scam/)**
  * 2TBの年額プランを契約中のユーザーが、Pixel 8 Pro購入特典の4ヶ月無料トライアルを有効化した事例です。
  * 元のプランが上位プランに強制変換された結果、支払い済みの契約期間が大幅短縮され、元のプランの権利が失われたと報告されています。

問題が長期化し、週に1回程度のペースでGoogle One ヘルプに進捗確認を求めても、定型文の返答しか得られないことがあります。GoogleとdocomoにGoogle Oneの不具合を問い合わせても、たらい回しにされるばかりで、問題が解決する見込みがありませんでした。

この事例では複数の購入特典・有料プランを重ねた後に不具合が発生しましたが、Googleが一般的な原因として『契約の重複』を公表していることまでは確認できていません。再発防止のため、自分の環境では新しい特典やプランを有効化する前に、既存プランとの併用可否、切り替え条件、残存期間の扱いを公式ページまたはサポートで確認します。

**Google Oneの契約を整理する場合**

通常は、まずGoogle Oneのプラン変更・解約手順と、購入元がGoogle Play / App Store / 携帯通信事業者などの第三者かを確認します。第三者経由の契約は、その提供元で管理が必要な場合があります。

Google公式ヘルプには、特定の契約移行や解約状況でGoogle Oneサービス自体を削除する手順もありますが、一般的な『不具合の初期化』として常用する操作ではありません。サービス削除はプラン関連データや設定等に影響するため、実行前に公式ヘルプとサポートで影響範囲を確認します。Google Drive、Gmail、Googleフォトの保存ファイルが操作直後に一括削除される、という意味ではありません。

* **参考サイト**： [r/GoogleOne｜Reddit](https://www.reddit.com/r/GoogleOne/)

---

## ChromeOS Chrome 拡張機能
* **[Manifest V2 のサポート タイムライン（サポート終了済み）](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)**

 ChromeOSおよびChromeブラウザにおいて、Manifest V2拡張機能のサポートは順次終了・無効化されています。

* **[Chrome Web Store 拡張機能](https://chromewebstore.google.com/category/extensions)**

Chrome Web Store外から入手した拡張機能を自分でインストールする場合は、拡張機能ページの右上にあるトグルスイッチを切り替えて**デベロッパーモード**を有効にする必要があります。

**Violentmonkeyの導入**

ブラウザに機能を追加するUserScriptを管理・実行できる無料のブラウザ拡張機能です。
* **[Violentmonkey](https://chromewebstore.google.com/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)**
* **[Greasy Fork‐便利で安全なUserScript](https://greasyfork.org/ja)**

Chrome 138以降でViolentmonkeyを使用する場合は、`chrome://extensions` > Violentmonkey > **詳細** > **ユーザースクリプトを許可する** を有効にします。Chrome 138未満では、代わりに拡張機能ページの**デベロッパーモード**を有効にする必要があります。

**❗️留意点**

 以下のブラウザ拡張機能やUserScriptは、全てをインストールして使用しているわけではありません。ブラウザ拡張機能やUserScriptを入れすぎると競合を起こしてトラブルの原因になるため、数は少なければ少ないほど良いです。

* ブラウザ拡張機能の競合を疑いながらも問題の切り分けができず、AdGuard Filtersに相談したIssuesの例。：[#228169](https://github.com/AdguardTeam/AdguardFilters/issues/228169)
* Gmail 「システムで問題が発生しました（#2014）」。：[Reddit報告例](https://www.reddit.com/r/techsupport/comments/1b4rocl/oops_the_system_encountered_a_problem_2014/?tl=ja)

▶ 断定はできませんが、[PhotoShow](https://chromewebstore.google.com/detail/photoshow/mgpdnhlllbpncjpgokgfogidhoegebod) が原因だった可能性が高く、同様のブラウザ拡張機能でも同じ不具合が起きるかもしれません。

### コンテンツブロック・プライバシー関連
* **[AdGuard Extra](https://github.com/AdguardTeam/AdGuardExtra)**：Anti-Adblocker対策用UserScript ‐ 対象サイトはFacebook、Twitchなど。
* **[AdGuard ブラウザ拡張機能 MV3対応版](https://chromewebstore.google.com/detail/adguard-%E5%BA%83%E5%91%8A%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=ja)**：Chrome 拡張機能。（詳細後述）
* **[tinyShield](https://github.com/List-KR/tinyShield/blob/main/README.ja.md)**：Ad-Shield対策用のUserScript ‐ Tampermonkeyで購読して、Manifest V3のフィルタ更新制限を回避する。
* **[uBlacklist](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)**：検索結果のフィルタリング、指定したサイトの検索結果を非表示にする。（詳細後述）

### YouTube関連
* **[Enhancer for YouTube™](https://chromewebstore.google.com/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle)**：再生速度や音量のマウス制御、画質固定、テーマ変更、コメント非表示などYouTubeの機能を強化する。
* **[SponsorBlock for YouTube-動画の広告シーンを自動スキップ](https://chromewebstore.google.com/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone)**：YouTube動画内のスポンサーセグメントやイントロなどを、ユーザーの報告に基づき自動でスキップする。

### ショッピング関連
* **[Amazonレビュー信頼度判定 & 無限スクロール（サクラ識別 / 品質チェック）](https://greasyfork.org/ja/scripts/561755)**：Amazonのレビュアー投稿履歴を分析し、信頼度をS〜Dランクで視覚化。信頼度フィルタリング機能や、レビュー一覧の無限スクロール化も提供。
* **[Condler](https://chromewebstore.google.com/detail/condler/ejjdbndmmongojeafjlilnchmkppbeap)**：Amazon検索結果の左側サイドバーに、並び替えやAmazon公式出品のみに絞り込むボタンを追加する。
* **[Keepa - Amazon Price Tracker](https://chromewebstore.google.com/detail/keepa-amazon-price-tracke/neebplgakaahbhdphmkckjjcegoiijjo)**：Amazon商品の価格履歴グラフをページ上に表示し、設定した価格になると通知を受け取れる。
* **[Knockoff — Amazon Brand Filter](https://chromewebstore.google.com/detail/knockoff-%E2%80%94-amazon-brand-f/pjgickchbiikhdfpmecaabkphmofpdce)**：Amazon検索結果から、指定したブランドや出品者を除外できる。
* **[サクラチェッカーをAmazon内に直接表示 🔍️](https://greasyfork.org/ja/scripts/533121)**：Amazonの商品ページに、サクラチェッカーのスコアと判定結果を高速で自動表示する。

### 検索・ブラウジング補助
* **[Buster: Captcha Solver for Humans](https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl)**：音声チャレンジを利用してCAPTCHAの解答を支援する拡張機能。対象サービスの利用規約や仕様変更により利用できない場合があります。
* **[Cesturefy](https://chromewebstore.google.com/detail/cesturefy-navigate-operat/bifgfhokfobhebifcogneljkpaaloonp)**：マウス、ロッカー、ホイールジェスチャーでブラウザ操作を効率化する拡張機能。
* **[google-search-title-qualified](https://chromewebstore.google.com/detail/google-search-title-quali/bjcnnhojddnonjmhlpdjcdcfmofliagb)**：Google検索結果にサイト本来のタイトルを表示させる。
* **[Search Result Previews](https://chromewebstore.google.com/detail/search-result-previews/cedcejfiniojnlhlfhcppenochinijfo)**：検索結果のリンク横にウェブサイトのプレビュー画像（サムネイル）を表示させる。
* **[uBlacklist Subscription - Japanese](https://github.com/eai04191/ublacklist-subscription-ja)**：uBlacklist用の購読リスト。日本語圏の検索結果から不要なサイトを除外する。

---

## ChromeOS Chrome テーマ
* **[Chrome Web Store テーマ](https://chromewebstore.google.com/category/themes)**
* **[Dark Horizon](https://chromewebstore.google.com/detail/dark-horizon/ncjjeokpcnllmmbbipeaagmdpdpiadin)**：Chrome標準テーマに近い外観を、より暗い配色にしたシンプルなダークテーマ。
* **[Royal Desert Sand](https://chromewebstore.google.com/detail/royal-desert-sand/nnieplejkjaodhemceganohmdkfekkem)**：デザートサンド（砂漠の砂）系の落ち着いた暖色とロイヤルブルーを組み合わせた、シンプルで上品なChromeテーマ。

---

## ChromeOS Chrome アプリ
* **[Chrome アプリのサポート終了（順次終了済み）](https://support.google.com/chrome/a/answer/15950395?hl=ja)**

