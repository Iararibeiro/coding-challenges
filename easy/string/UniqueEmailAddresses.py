#1 <= emails.length <= 100
#1 <= emails[i].length <= 100
#email[i] consist of lowercase English letters, '+', '.' and '@'.
#Each emails[i] contains exactly one '@' character.
#All local and domain names are non-empty.
#Local names do not start with a '+' character.

def numUniqueEmails(emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.replace('.', '').split('+')[0]
        unique_email = local + '@' + domain
        unique_emails.add(unique_email)
    
    return len(unique_emails)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))