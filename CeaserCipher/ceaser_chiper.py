class CeaserChiper:

    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        return "".join( [self.encrypt_char(x) for x in message] )


    def descrypt(self, message):
        return "".join( [self.descrypt_char(x) for x in message] )


    def encrypt_char(self, char):
        if self._is_base_case(char):
            return ""

        if ord(char) > ord("Z") - self.shift:
            return chr( ord("A") + (self.shift - 1 - (ord("Z") - ord(char))))

        return chr(ord(char) + self.shift)


    def descrypt_char(self, char):
        if self._is_base_case(char):
            return ""

        if ord(char) < ord("A") + self.shift:
            return chr( ord("Z") - (self.shift - 1 - (ord(char) - ord("A"))))

        return chr(ord(char) - self.shift)



    def _is_base_case(self, char):
        if char == "" or char.islower():
            return True
