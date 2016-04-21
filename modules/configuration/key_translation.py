import pygame

# =============================================================================
# Name:       get_key_number(key_name)
# Arguments:  key_name = a name for the key in caps
# Purpose:    returns an if number corresponding to name of key
# =============================================================================
def get_key_number(key_name):
    known_keys = dict()
    known_keys["BACKSPACE"] = 8
    known_keys["TAB"] = 9
    known_keys["CLEAR"] = 12
    known_keys["RETURN"] = 13
    known_keys["PAUSE"] = 19
    known_keys["ESCAPE"] = 27
    known_keys["SPACE"] = 32
    known_keys["!"] = 33
    known_keys['"'] = 34
    known_keys["#"] = 35
    known_keys["$"] = 36
    known_keys["&"] = 38
    known_keys["'"] = 39
    known_keys["("] = 40
    known_keys[")"] = 41
    known_keys["*"] = 42
    known_keys["+"] = 43
    known_keys[","] = 44
    known_keys["-"] = 45
    known_keys["."] = 46
    known_keys["/"] = 47
    known_keys["0"] = 48
    known_keys["1"] = 49
    known_keys["2"] = 50
    known_keys["3"] = 51
    known_keys["4"] = 52
    known_keys["5"] = 53
    known_keys["6"] = 54
    known_keys["7"] = 55
    known_keys["8"] = 56
    known_keys["9"] = 57
    known_keys[":"] = 58
    known_keys[";"] = 59
    known_keys["<"] = 60
    known_keys["="] = 61
    known_keys[">"] = 62
    known_keys["?"] = 63
    known_keys["@"] = 64
    known_keys["["] = 91
    known_keys["\\"] = 92
    known_keys["]"] = 93
    known_keys["^"] = 94
    known_keys["_"] = 95
    known_keys["`"] = 96
    known_keys["A"] = 97
    known_keys["B"] = 98
    known_keys["C"] = 99
    known_keys["D"] = 100
    known_keys["E"] = 101
    known_keys["F"] = 102
    known_keys["G"] = 103
    known_keys["H"] = 104
    known_keys["I"] = 105
    known_keys["J"] = 106
    known_keys["K"] = 107
    known_keys["L"] = 108
    known_keys["M"] = 109
    known_keys["N"] = 110
    known_keys["O"] = 111
    known_keys["P"] = 112
    known_keys["Q"] = 113
    known_keys["R"] = 114
    known_keys["S"] = 115
    known_keys["T"] = 116
    known_keys["U"] = 117
    known_keys["V"] = 118
    known_keys["W"] = 119
    known_keys["X"] = 120
    known_keys["Y"] = 121
    known_keys["Z"] = 122
    known_keys["DELETE"] = 127
    known_keys["[0]"] = 256
    known_keys["[1]"] = 257
    known_keys["[2]"] = 258
    known_keys["[3]"] = 259
    known_keys["[4]"] = 260
    known_keys["[5]"] = 261
    known_keys["[6]"] = 262
    known_keys["[7]"] = 263
    known_keys["[8]"] = 264
    known_keys["[9]"] = 265
    known_keys["[.]"] = 266
    known_keys["[/]"] = 267
    known_keys["[*]"] = 268
    known_keys["[-]"] = 269
    known_keys["[+]"] = 270
    known_keys["ENTER"] = 271
    known_keys["EQUALS"] = 272
    known_keys["UP"] = 273
    known_keys["DOWN"] = 274
    known_keys["RIGHT"] = 275
    known_keys["LEFT"] = 276
    known_keys["INSERT"] = 277
    known_keys["HOME"] = 278
    known_keys["END"] = 279
    known_keys["PAGE UP"] = 280
    known_keys["PAGE DOWN"] = 281
    known_keys["F1"] = 282
    known_keys["F2"] = 283
    known_keys["F3"] = 284
    known_keys["F4"] = 285
    known_keys["F5"] = 286
    known_keys["F6"] = 287
    known_keys["F7"] = 288
    known_keys["F8"] = 289
    known_keys["F9"] = 290
    known_keys["F10"] = 291
    known_keys["F11"] = 292
    known_keys["F12"] = 293
    known_keys["F13"] = 294
    known_keys["F14"] = 295
    known_keys["F15"] = 296
    known_keys["NUMLOCK"] = 300
    known_keys["CAPS LOCK"] = 301
    known_keys["SCROLL LOCK"] = 302
    known_keys["RIGHT SHIFT"] = 303
    known_keys["LEFT SHIFT"] = 304
    known_keys["RIGHT CTRL"] = 305
    known_keys["LEFT CTRL"] = 306
    known_keys["RIGHT ALT"] = 307
    known_keys["LEFT ALT"] = 308
    known_keys["RIGHT META"] = 309
    known_keys["LEFT META"] = 310
    known_keys["LEFT SUPER"] = 311
    known_keys["RIGHT SUPER"] = 312
    known_keys["ALT GR"] = 313
    known_keys["COMPOSE"] = 314
    known_keys["HELP"] = 315
    known_keys["PRINT SCREEN"] = 316
    known_keys["SYS REQ"] = 317
    known_keys["BREAK"] = 318
    known_keys["MENU"] = 319
    known_keys["POWER"] = 320
    known_keys["EURO"] = 321
    known_keys["UNDO"] = 322
    return known_keys[key_name]
# =============================================================================


# =============================================================================
# Name:       get_key_name(key_number)
# Arguments:  key_number = an int value corresponding to key id
# Depends:    requires pygame gui to be started
# Purpose:    returns a name corresponding to number
# =============================================================================
def get_key_name(key_number):
    key_name = str(pygame.key.name(key_number))
    key_name.upper()
    return key_name
# =============================================================================





