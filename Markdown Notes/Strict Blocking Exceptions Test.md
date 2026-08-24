# Strict Blocking Exceptions Test

AdGuard / uBlock Origin の Strict blocking と例外ルールを扱う検証メモです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 公式仕様として確認できる範囲

- AdGuard の `$document` はメインドキュメントへのリクエストを対象にするネットワーク修飾子です。
- 例外ルールは `@@` を先頭に付けて記述します。
- uBlock Origin でも `document` はメインフレームのネットワークリクエストを対象にします。

実際のサイトでどの例外ルールがどのように作用するかは、使用中の製品、バージョン、他のフィルタ、サイト側の実装に依存します。そのため、特定サイトで観測した挙動や原因推測は仕様として一般化せず、本書から削除しました。

## 参照

- [AdGuard — How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [uBlock Origin Wiki — Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
