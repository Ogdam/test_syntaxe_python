from enum import Enum

class Constants(Enum):

    specialChars = [
        { "value": ' *a* '  ,  "name":"Equal"                , "regex": "=="  },
        { "value": ' *b* '  ,  "name":"InfOrEqual"           , "regex": ">="  },
        { "value": ' *c* '  ,  "name":"SupOrEqual"           , "regex": "<="  },
        { "value": ' *d* '  ,  "name":"Different"            , "regex": "!="  },
        { "value": ' *=* '  ,  "name":"affectation"          , "regex": "="  },
        { "value": ' *<* '  ,  "name":"inferieur"            , "regex": ">"  },
        { "value": ' *>* '  ,  "name":"superieur"            , "regex": "<"  },
        { "value": ' *\v* ' ,  "name":"lineReturn"           , "regex": "\v" },
        { "value": ' *\t* ' ,  "name":"tabulation"           , "regex": "\t" },
        { "value": ' *:* '  ,  "name":"definitions"          , "regex": ":"  },
        { "value": ' *(* '  ,  "name":"openParenthese"       , "regex": "("  },
        { "value": ' *)* '  ,  "name":"closeParenthese"      , "regex": ")"  },
        { "value": ' *{* '  ,  "name":"openAcolade"          , "regex": "{"  },
        { "value": ' *}* '  ,  "name":"closeAcolade"         , "regex": "}"  },
        { "value": ' *[* '  ,  "name":"openCrochet"          , "regex": "["  },
        { "value": ' *]* '  ,  "name":"closeCrochet"         , "regex": "]"  },
        { "value": ' *,* '  ,  "name":"comma"                , "regex": ","  },
        { "value": ' *\"* '  ,  "name":"quote"               , "regex": '\"'  }
    ]

    typeWord = "Word"
    typeNumber = "Number"
    endOfLine = "endOfLine"

    errorToken = "No token found in file"
