# AdGuard Custom Rules Reference

AdGuardカスタムルールの簡易リファレンスです。詳細な仕様と製品別対応状況は、AdGuard公式ドキュメントを正本として確認してください。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## ネットワークルール

| 構文 | 用途 |
| :--- | :--- |
| `||example.com^` | ドメインに一致するネットワークルール |
| `@@||example.com^` | 例外ルール |
| `$document` | メインドキュメントのリクエスト |
| `$subdocument` | サブドキュメントのリクエスト |
| `$script` | Scriptリクエスト |
| `$image` | Imageリクエスト |
| `$xmlhttprequest` | XMLHttpRequest / Fetch系リクエスト |
| `$third-party` | サードパーティリクエスト |
| `$domain=` | 適用元ドメインを限定 |
| `$denyallow=` | 特定ドメインを除外して適用 |
| `$to=` | リクエスト送信先を限定 |
| `$app=` | 対応製品で対象アプリを限定 |
| `$removeparam` | URLパラメータを除去 |
| `$redirect` | 対応するリダイレクトリソースへ置換 |
| `$csp` | Content-Security-Policyを適用 |
| `$replace` | 対応製品でレスポンス本文を置換 |

製品ごとに対応する修飾子が異なります。特にブラウザ拡張機能とCoreLibsベース製品では利用可能な機能に差があります。

## 要素隠蔽

| 構文 | 用途 |
| :--- | :--- |
| `example.com##.ad` | 指定サイトでCSSセレクタに一致する要素を隠す |
| `example.com#@#.ad` | 要素隠蔽の例外 |
| `example.com#?#...` | Extended CSSルール |
| `example.com#$#...` | CSSスタイルを適用するルール |

Extended CSSなどの高度な構文は、対応製品・バージョンを公式ドキュメントで確認してください。

## Scriptlets

AdGuardはScriptletルールをサポートしますが、利用できるScriptletと構文は製品・バージョンによって異なります。利用前に公式Scriptletsリファレンスを確認してください。

## DNSフィルタリング

DNSフィルタリングでは、Webフィルタリング用の全修飾子を利用できるわけではありません。DNS向け構文は専用リファレンスを確認してください。

## 公式ドキュメント

- [How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [Scriptlets](https://adguard.com/kb/general/ad-filtering/create-own-filters/scriptlets/)
- [DNS filtering rules syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/)
- [AdGuard Browser Extension MV3](https://adguard.com/kb/adguard-browser-extension/mv3-version/)
