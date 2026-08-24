# DNS Blocklist Guide

DNSブロックリストの形式と配布元を簡潔に整理します。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 主な形式

### Hosts形式
`0.0.0.0 example.com` のようにIPアドレスとホスト名を記述します。対応範囲やサブドメインの扱いは、読み込むソフトウェアの実装に依存します。

### Domains-only形式
`example.com` のようにドメイン名だけを1行ずつ記述します。例外、正規表現、リソース種別などの高度な条件は表現できません。

### AdGuard DNSフィルタ構文
AdGuard DNSフィルタリングでは、`||example.com^` や `@@||example.com^` など、AdGuardが定義するDNSフィルタ構文を利用できます。利用可能な構文はAdGuard公式ドキュメントを確認してください。

## 配布元

### AdGuard DNS filter
AdGuardが公開・保守するDNSフィルタです。

- [AdGuard DNS filter repository](https://github.com/AdguardTeam/AdGuardSDNSFilter)
- [AdGuard DNS filtering rules syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/)

### HaGeZi DNS Blocklists
HaGeZiが公開・保守するDNSブロックリストです。複数の強度と配布形式があります。各リストの位置付けと対応形式は、作者のREADMEを確認してください。

- [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)

## 運用上の注意

- フィルタ形式は、利用するDNSブロッカーが公式に対応しているものを選びます。
- 異なる構文を想定したリストをそのまま流用すると、無視されるルールや意図しないブロックが発生する可能性があります。
- 「どのリストが最適か」という評価は利用環境と許容できる誤ブロック率に依存するため、本書では特定のリストを一律に推奨しません。
