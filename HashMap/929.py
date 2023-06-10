class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []
        for email in emails:
            localName, domainName = email.split("@")
            # +以降は無視
            localName = localName.split("+")[0]
            # 「.」を無視
            localName = "".join(localName.split("."))
            ans.append(f"{localName}@{domainName}")
        return len(set(ans))