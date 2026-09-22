class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails: set[str] = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            normalized: str = local + "@" + domain
            unique_emails.add(normalized)
        return len(unique_emails)