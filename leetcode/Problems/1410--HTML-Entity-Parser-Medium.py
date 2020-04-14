
#     Quotation Mark: the entity is &quot; and symbol character is ".
#     Single Quote Mark: the entity is &apos; and symbol character is '.
#     Ampersand: the entity is &amp; and symbol character is &.
#     Greater Than Sign: the entity is &gt; and symbol character is >.
#     Less Than Sign: the entity is &lt; and symbol character is <.
#     Slash: the entity is &frasl; and symbol character is /.

class Solution:
    def entityParser(self, text: str) -> str:

        answer = text.replace('&quot;', '"')
        answer = answer.replace('&apos;', "'")
        
        answer = answer.replace('&gt;', '>')
        answer = answer.replace('&lt;', '<')
        answer = answer.replace('&frasl;', '/')
        answer = answer.replace('&amp;', "&")
        return answer

        