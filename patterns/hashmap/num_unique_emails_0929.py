#929. Unique Email Addresses
def numUniqueEmails(emails):
    unique = set()
    for email in emails:
        local, domain = email.split('@')
        # THOUGHTS: split on '@' FIRST. The '+' and '.' rules apply only to the
        #   LOCAL part — never the domain. Splitting the whole email on '+' would
        #   drop everything after '+', including "@domain"
        #   ("a+alex@x.com".split('+')[0] == "a"), and the domain's dots are
        #   significant, so they must be kept.
        local = local.split('+')[0].replace('.', '')
        unique.add(local + '@' + domain)

    return len(unique)
