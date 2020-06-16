"""
1. Yes

X                    X
X  X              X  X
X  X  X        X  X  X
   X  X  X  X  X  X
      X  X  X  X
         X  X
"""
ascii_yes = """\
        \n\
X      X\n\
XX    XX\n\
XXX  XXX\n\
 XXXXXX \n\
  XXXX  \n\
   XX   \n\
        \
"""

"""
2. No
X  X              X  X
X  X  X        X  X  X
   X  X  X  X  X  X
      X  X  X  X
      X  X  X  X
   X  X  X  X  X  X
X  X  X        X  X  X
X  X              X  X
"""
ascii_no = """\
XX    XX\n\
XXX  XXX\n\
 XXXXXX \n\
  XXXX  \n\
  XXXX  \n\
 XXXXXX \n\
XXX  XXX\n\
XX    XX\
"""
"""
4. Face

   X  X        X  X
   X  X        X  X


   X  X  X  X  X  X
   X  X  X  X  X  X

"""
ascii_me = """\
        \n\
 XX  XX \n\
 XX  XX \n\
        \n\
        \n\
 XXXXXX \n\
 XXXXXX \n\
        \
"""
ascii_why = """\
  XXXX  \n\
 XX  XX \n\
  X   X \n\
     XX \n\
   XX   \n\
  XX    \n\
        \n\
  XX    \
"""

ascii_pics = {"yes": ascii_yes, "no": ascii_no, "why": ascii_why, "me": ascii_me}

################################################################################

"""
3. HAL9000

         X  X
      X  X  X  X
   X  X  X  X  X  X
   X  X  X  X  X  X
      X  X  X  X
         X  X


4. Face

   X  X        X  X
   X  X        X  X


   X  X  X  X  X  X
   X  X  X  X  X  X


5. Siri orb animation

         X  X
      X  X  X  X
   X  X  X  X  X  X
   X  X  X  X  X  X
      X  X  X  X
         X  X

7. Emojis?
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X
X  X  X  X  X  X  X  X

"""

SQUARE_GAUSS_4 = [
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0112, 0.0112, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0112, 0.0112, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0288, 0.0288, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0288, 0.0288, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0661, 0.0661, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0661, 0.0661, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.1358, 0.1358, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.1358, 0.1358, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.001, 0.001, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.001, 0.25, 0.25, 0.001, 0.0, 0.0],
  [0.0, 0.0, 0.001, 0.25, 0.25, 0.001, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.001, 0.001, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0003, 0.0118, 0.0118, 0.0003, 0.0, 0.0],
  [0.0, 0.0, 0.0118, 0.4118, 0.4118, 0.0118, 0.0, 0.0],
  [0.0, 0.0, 0.0118, 0.4118, 0.4118, 0.0118, 0.0, 0.0],
  [0.0, 0.0, 0.0003, 0.0118, 0.0118, 0.0003, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0002, 0.0015, 0.0015, 0.0002, 0.0, 0.0],
  [0.0, 0.0002, 0.0112, 0.0825, 0.0825, 0.0112, 0.0002, 0.0],
  [0.0, 0.0015, 0.0825, 0.6071, 0.6071, 0.0825, 0.0015, 0.0],
  [0.0, 0.0015, 0.0825, 0.6071, 0.6071, 0.0825, 0.0015, 0.0],
  [0.0, 0.0002, 0.0112, 0.0825, 0.0825, 0.0112, 0.0002, 0.0],
  [0.0, 0.0, 0.0002, 0.0015, 0.0015, 0.0002, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0003, 0.0016, 0.0039, 0.0039, 0.0016, 0.0003, 0.0],
  [0.0003, 0.0039, 0.023, 0.0559, 0.0559, 0.023, 0.0039, 0.0003],
  [0.0016, 0.023, 0.1358, 0.3299, 0.3299, 0.1358, 0.023, 0.0016],
  [0.0039, 0.0559, 0.3299, 0.8011, 0.8011, 0.3299, 0.0559, 0.0039],
  [0.0039, 0.0559, 0.3299, 0.8011, 0.8011, 0.3299, 0.0559, 0.0039],
  [0.0016, 0.023, 0.1358, 0.3299, 0.3299, 0.1358, 0.023, 0.0016],
  [0.0003, 0.0039, 0.023, 0.0559, 0.0559, 0.023, 0.0039, 0.0003],
  [0.0, 0.0003, 0.0016, 0.0039, 0.0039, 0.0016, 0.0003, 0.0]],
 [[0.0661, 0.1285, 0.2003, 0.25, 0.25, 0.2003, 0.1285, 0.0661],
  [0.1285, 0.25, 0.3896, 0.4863, 0.4863, 0.3896, 0.25, 0.1285],
  [0.2003, 0.3896, 0.6071, 0.7579, 0.7579, 0.6071, 0.3896, 0.2003],
  [0.25, 0.4863, 0.7579, 0.9461, 0.9461, 0.7579, 0.4863, 0.25],
  [0.25, 0.4863, 0.7579, 0.9461, 0.9461, 0.7579, 0.4863, 0.25],
  [0.2003, 0.3896, 0.6071, 0.7579, 0.7579, 0.6071, 0.3896, 0.2003],
  [0.1285, 0.25, 0.3896, 0.4863, 0.4863, 0.3896, 0.25, 0.1285],
  [0.0661, 0.1285, 0.2003, 0.25, 0.25, 0.2003, 0.1285, 0.0661]],
 [[0.0661, 0.1285, 0.2003, 0.25, 0.25, 0.2003, 0.1285, 0.0661],
  [0.1285, 0.25, 0.3896, 0.4863, 0.4863, 0.3896, 0.25, 0.1285],
  [0.2003, 0.3896, 0.6071, 0.7579, 0.7579, 0.6071, 0.3896, 0.2003],
  [0.25, 0.4863, 0.7579, 0.9461, 0.9461, 0.7579, 0.4863, 0.25],
  [0.25, 0.4863, 0.7579, 0.9461, 0.9461, 0.7579, 0.4863, 0.25],
  [0.2003, 0.3896, 0.6071, 0.7579, 0.7579, 0.6071, 0.3896, 0.2003],
  [0.1285, 0.25, 0.3896, 0.4863, 0.4863, 0.3896, 0.25, 0.1285],
  [0.0661, 0.1285, 0.2003, 0.25, 0.25, 0.2003, 0.1285, 0.0661]],
 [[0.0, 0.0003, 0.0016, 0.0039, 0.0039, 0.0016, 0.0003, 0.0],
  [0.0003, 0.0039, 0.023, 0.0559, 0.0559, 0.023, 0.0039, 0.0003],
  [0.0016, 0.023, 0.1358, 0.3299, 0.3299, 0.1358, 0.023, 0.0016],
  [0.0039, 0.0559, 0.3299, 0.8011, 0.8011, 0.3299, 0.0559, 0.0039],
  [0.0039, 0.0559, 0.3299, 0.8011, 0.8011, 0.3299, 0.0559, 0.0039],
  [0.0016, 0.023, 0.1358, 0.3299, 0.3299, 0.1358, 0.023, 0.0016],
  [0.0003, 0.0039, 0.023, 0.0559, 0.0559, 0.023, 0.0039, 0.0003],
  [0.0, 0.0003, 0.0016, 0.0039, 0.0039, 0.0016, 0.0003, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0002, 0.0015, 0.0015, 0.0002, 0.0, 0.0],
  [0.0, 0.0002, 0.0112, 0.0825, 0.0825, 0.0112, 0.0002, 0.0],
  [0.0, 0.0015, 0.0825, 0.6071, 0.6071, 0.0825, 0.0015, 0.0],
  [0.0, 0.0015, 0.0825, 0.6071, 0.6071, 0.0825, 0.0015, 0.0],
  [0.0, 0.0002, 0.0112, 0.0825, 0.0825, 0.0112, 0.0002, 0.0],
  [0.0, 0.0, 0.0002, 0.0015, 0.0015, 0.0002, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0003, 0.0118, 0.0118, 0.0003, 0.0, 0.0],
  [0.0, 0.0, 0.0118, 0.4118, 0.4118, 0.0118, 0.0, 0.0],
  [0.0, 0.0, 0.0118, 0.4118, 0.4118, 0.0118, 0.0, 0.0],
  [0.0, 0.0, 0.0003, 0.0118, 0.0118, 0.0003, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.001, 0.001, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.001, 0.25, 0.25, 0.001, 0.0, 0.0],
  [0.0, 0.0, 0.001, 0.25, 0.25, 0.001, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.001, 0.001, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.1358, 0.1358, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.1358, 0.1358, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0661, 0.0661, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0661, 0.0661, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0288, 0.0288, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0288, 0.0288, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
 [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0112, 0.0112, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0112, 0.0112, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
]

SQUARE_GAUSS = [
 [[2.6118953774438405e-96, 6.684181585222283e-73, 2.694283024543055e-57, 1.7105694144590234e-49, 1.7105694144590234e-49, 2.694283024543055e-57, 6.684181585222283e-73, 2.6118953774438405e-96],
       [6.684181585222283e-73, 1.7105694144590234e-49, 6.895022340310091e-34, 4.377570663477814e-26, 4.377570663477814e-26, 6.895022340310091e-34, 1.7105694144590234e-49, 6.684181585222283e-73],
    [2.694283024543055e-57, 6.895022340310091e-34, 2.7792694451051804e-18, 1.764526318887254e-10, 1.764526318887254e-10, 2.7792694451051804e-18, 6.895022340310091e-34, 2.694283024543055e-57],
       [1.7105694144590234e-49, 4.377570663477814e-26, 1.764526318887254e-10, 0.011202775375123661, 0.011202775375123661, 1.764526318887254e-10, 4.377570663477814e-26, 1.7105694144590234e-49],
       [1.7105694144590234e-49, 4.377570663477814e-26, 1.764526318887254e-10, 0.011202775375123661, 0.011202775375123661, 1.764526318887254e-10, 4.377570663477814e-26, 1.7105694144590234e-49],
       [2.694283024543055e-57, 6.895022340310091e-34, 2.7792694451051804e-18, 1.764526318887254e-10, 1.764526318887254e-10, 2.7792694451051804e-18, 6.895022340310091e-34, 2.694283024543055e-57],
       [6.684181585222283e-73, 1.7105694144590234e-49, 6.895022340310091e-34, 4.377570663477814e-26, 4.377570663477814e-26, 6.895022340310091e-34, 1.7105694144590234e-49, 6.684181585222283e-73],
       [2.6118953774438405e-96, 6.684181585222283e-73, 2.694283024543055e-57, 1.7105694144590234e-49, 1.7105694144590234e-49, 2.694283024543055e-57, 6.684181585222283e-73, 2.6118953774438405e-96]
   ],
   [
       [3.003272143191179e-76, 9.394585459592318e-58, 2.009399286955082e-45, 2.938735877055727e-39, 2.938735877055727e-39, 2.009399286955082e-45, 9.394585459592318e-58, 3.003272143191179e-76],
       [9.394585459592318e-58, 2.938735877055727e-39, 6.285635275025237e-27, 9.192708493887553e-21, 9.192708493887553e-21, 6.285635275025237e-27, 2.938735877055727e-39, 9.394585459592318e-58],
       [2.009399286955082e-45, 6.285635275025237e-27, 1.3444287769823358e-14, 1.9662200074984073e-08, 1.9662200074984073e-08, 1.3444287769823358e-14, 6.285635275025237e-27, 2.009399286955082e-45],
       [2.938735877055727e-39, 9.192708493887553e-21, 1.9662200074984073e-08, 0.028755864082027342, 0.028755864082027342, 1.9662200074984073e-08, 9.192708493887553e-21, 2.938735877055727e-39],
       [2.938735877055727e-39, 9.192708493887553e-21, 1.9662200074984073e-08, 0.028755864082027342, 0.028755864082027342, 1.9662200074984073e-08, 9.192708493887553e-21, 2.938735877055727e-39],
       [2.009399286955082e-45, 6.285635275025237e-27, 1.3444287769823358e-14, 1.9662200074984073e-08, 1.9662200074984073e-08, 1.3444287769823358e-14, 6.285635275025237e-27, 2.009399286955082e-45],
       [9.394585459592318e-58, 2.938735877055727e-39, 6.285635275025237e-27, 9.192708493887553e-21, 9.192708493887553e-21, 6.285635275025237e-27, 2.938735877055727e-39, 9.394585459592318e-58],
       [3.003272143191179e-76, 9.394585459592318e-58, 2.009399286955082e-45, 2.938735877055727e-39, 2.938735877055727e-39, 2.009399286955082e-45, 9.394585459592318e-58, 3.003272143191179e-76]
   ],
   [
       [1.5071567844635535e-58, 2.1807678146028544e-44, 6.010492961557393e-35, 3.1554436208840535e-30, 3.1554436208840535e-30, 6.010492961557393e-35, 2.1807678146028544e-44, 1.5071567844635535e-58],
       [2.1807678146028544e-44, 3.1554436208840535e-30, 8.696832164761637e-21, 4.565742569156177e-16, 4.565742569156177e-16, 8.696832164761637e-21, 3.1554436208840535e-30, 2.1807678146028544e-44],
       [6.010492961557393e-35, 8.696832164761637e-21, 2.3969653332244333e-11, 1.2583808047989792e-06, 1.2583808047989792e-06, 2.3969653332244333e-11, 8.696832164761637e-21, 6.010492961557393e-35],
       [3.1554436208840535e-30, 4.565742569156177e-16, 1.2583808047989792e-06, 0.06606362753508628, 0.06606362753508628, 1.2583808047989792e-06, 4.565742569156177e-16, 3.1554436208840535e-30],
       [3.1554436208840535e-30, 4.565742569156177e-16, 1.2583808047989792e-06, 0.06606362753508628, 0.06606362753508628, 1.2583808047989792e-06, 4.565742569156177e-16, 3.1554436208840535e-30],
       [6.010492961557393e-35, 8.696832164761637e-21, 2.3969653332244333e-11, 1.2583808047989792e-06, 1.2583808047989792e-06, 2.3969653332244333e-11, 8.696832164761637e-21, 6.010492961557393e-35],
       [2.1807678146028544e-44, 3.1554436208840535e-30, 8.696832164761637e-21, 4.565742569156177e-16, 4.565742569156177e-16, 8.696832164761637e-21, 3.1554436208840535e-30, 2.1807678146028544e-44],
       [1.5071567844635535e-58, 2.1807678146028544e-44, 6.010492961557393e-35, 3.1554436208840535e-30, 3.1554436208840535e-30, 6.010492961557393e-35, 2.1807678146028544e-44, 1.5071567844635535e-58]
  ],
  [[3.3010113067809964e-43, 8.360719670133873e-33, 7.21065575178869e-26, 2.117582368135768e-22, 2.117582368135768e-22, 7.21065575178869e-26, 8.360719670133873e-33, 3.3010113067809964e-43],
  [8.360719670133873e-33, 2.117582368135768e-22, 1.8262970276624776e-15, 5.363360168452738e-12, 5.363360168452738e-12, 1.8262970276624776e-15, 2.117582368135768e-22, 8.360719670133873e-33],
  [7.21065575178869e-26, 1.8262970276624776e-15, 1.5750796207210184e-08, 4.6255998733837856e-05, 4.6255998733837856e-05, 1.5750796207210184e-08, 1.8262970276624776e-15, 7.21065575178869e-26],
  [2.117582368135768e-22, 5.363360168452738e-12, 4.6255998733837856e-05, 0.1358418578157573, 0.1358418578157573, 4.6255998733837856e-05, 5.363360168452738e-12, 2.117582368135768e-22],
  [2.117582368135768e-22, 5.363360168452738e-12, 4.6255998733837856e-05, 0.1358418578157573, 0.1358418578157573, 4.6255998733837856e-05, 5.363360168452738e-12, 2.117582368135768e-22],
  [7.21065575178869e-26, 1.8262970276624776e-15, 1.5750796207210184e-08, 4.6255998733837856e-05, 4.6255998733837856e-05, 1.5750796207210184e-08, 1.8262970276624776e-15, 7.21065575178869e-26],
  [8.360719670133873e-33, 2.117582368135768e-22, 1.8262970276624776e-15, 5.363360168452738e-12, 5.363360168452738e-12, 1.8262970276624776e-15, 2.117582368135768e-22, 8.360719670133873e-33],
  [3.3010113067809964e-43, 8.360719670133873e-33, 7.21065575178869e-26, 2.117582368135768e-22, 2.117582368135768e-22, 7.21065575178869e-26, 8.360719670133873e-33, 3.3010113067809964e-43]],
 [[3.1554436208840535e-30, 5.2939559203394e-23, 3.4694469519536088e-18, 8.881784197001244e-16, 8.881784197001244e-16, 3.4694469519536088e-18, 5.2939559203394e-23, 3.1554436208840535e-30],
  [5.2939559203394e-23, 8.881784197001244e-16, 5.820766091346745e-11, 1.4901161193847676e-08, 1.4901161193847676e-08, 5.820766091346745e-11, 8.881784197001244e-16, 5.2939559203394e-23],
  [3.4694469519536088e-18, 5.820766091346745e-11, 3.814697265625001e-06, 0.0009765625, 0.0009765625, 3.814697265625001e-06, 5.820766091346745e-11, 3.4694469519536088e-18],
  [8.881784197001244e-16, 1.4901161193847676e-08, 0.0009765625, 0.25, 0.25, 0.0009765625, 1.4901161193847676e-08, 8.881784197001244e-16], [8.881784197001244e-16, 1.4901161193847676e-08, 0.0009765625, 0.25, 0.25, 0.0009765625, 1.4901161193847676e-08,
   8.881784197001244e-16], [3.4694469519536088e-18, 5.820766091346745e-11, 3.814697265625001e-06, 0.0009765625, 0.0009765625, 3.814697265625001e-06, 5.820766091346745e-11,
   3.4694469519536088e-18],
  [5.2939559203394e-23, 8.881784197001244e-16, 5.820766091346745e-11, 1.4901161193847676e-08, 1.4901161193847676e-08, 5.820766091346745e-11, 8.881784197001244e-16, 5.2939559203394e-23],
  [3.1554436208840535e-30, 5.2939559203394e-23, 3.4694469519536088e-18, 8.881784197001244e-16, 8.881784197001244e-16, 3.4694469519536088e-18, 5.2939559203394e-23, 3.1554436208840535e-30]],
 [[1.3164327314818958e-19, 5.536297320393433e-15, 6.6952463430416106e-12, 2.328306436538698e-10, 2.328306436538698e-10, 6.6952463430416106e-12, 5.536297320393433e-15, 1.3164327314818958e-19],
  [5.536297320393433e-15, 2.328306436538698e-10, 2.8157059226740155e-07, 9.791762524131055e-06, 9.791762524131055e-06, 2.8157059226740155e-07, 2.328306436538698e-10, 5.536297320393433e-15],
  [6.6952463430416106e-12, 2.8157059226740155e-07, 0.00034051359041757954, 0.01184153567586249, 0.01184153567586249, 0.00034051359041757954, 2.8157059226740155e-07, 6.6952463430416106e-12],
  [2.328306436538698e-10, 9.791762524131055e-06, 0.01184153567586249, 0.41179550863378656, 0.41179550863378656, 0.01184153567586249, 9.791762524131055e-06, 2.328306436538698e-10],
  [2.328306436538698e-10, 9.791762524131055e-06, 0.01184153567586249, 0.41179550863378656, 0.41179550863378656, 0.01184153567586249, 9.791762524131055e-06, 2.328306436538698e-10],
  [6.6952463430416106e-12, 2.8157059226740155e-07, 0.00034051359041757954, 0.01184153567586249, 0.01184153567586249, 0.00034051359041757954, 2.8157059226740155e-07, 6.6952463430416106e-12],
  [5.536297320393433e-15, 2.328306436538698e-10, 2.8157059226740155e-07, 9.791762524131055e-06, 9.791762524131055e-06, 2.8157059226740155e-07, 2.328306436538698e-10, 5.536297320393433e-15],
  [1.3164327314818958e-19, 5.536297320393433e-15, 6.6952463430416106e-12, 2.328306436538698e-10, 2.328306436538698e-10, 6.6952463430416106e-12, 5.536297320393433e-15, 1.3164327314818958e-19]],
 [[2.3969653332244417e-11, 9.562268089971774e-09, 5.1819556356719e-07, 3.814697265625008e-06, 3.814697265625008e-06, 5.1819556356719e-07, 9.562268089971774e-09, 2.3969653332244417e-11],
  [9.562268089971774e-09, 3.814697265625008e-06, 0.0002067249297760079, 0.0015218058196494156, 0.0015218058196494156, 0.0002067249297760079, 3.814697265625008e-06, 9.562268089971774e-09],
  [5.1819556356719e-07, 0.0002067249297760079, 0.011202775375123661, 0.0824692444233059, 0.0824692444233059, 0.011202775375123661, 0.0002067249297760079, 5.1819556356719e-07],
  [3.814697265625008e-06, 0.0015218058196494156, 0.0824692444233059, 0.6070974421975235, 0.6070974421975235, 0.0824692444233059, 0.0015218058196494156, 3.814697265625008e-06],
  [3.814697265625008e-06, 0.0015218058196494156, 0.0824692444233059, 0.6070974421975235, 0.6070974421975235, 0.0824692444233059, 0.0015218058196494156, 3.814697265625008e-06],
  [5.1819556356719e-07, 0.0002067249297760079, 0.011202775375123661, 0.0824692444233059, 0.0824692444233059, 0.011202775375123661, 0.0002067249297760079, 5.1819556356719e-07],
  [9.562268089971774e-09, 3.814697265625008e-06, 0.0002067249297760079, 0.0015218058196494156, 0.0015218058196494156, 0.0002067249297760079, 3.814697265625008e-06, 9.562268089971774e-09],
  [2.3969653332244417e-11, 9.562268089971774e-09, 5.1819556356719e-07, 3.814697265625008e-06, 3.814697265625008e-06, 5.1819556356719e-07, 9.562268089971774e-09, 2.3969653332244417e-11]],
 [[1.9048012525964537e-05, 0.00027277518019341347, 0.0016085762056007283, 0.003906250000000001, 0.003906250000000001, 0.0016085762056007283, 0.00027277518019341347, 1.9048012525964537e-05],
  [0.00027277518019341347, 0.003906250000000001, 0.023035456520173463, 0.05593906693299829, 0.05593906693299829, 0.023035456520173463, 0.003906250000000001, 0.00027277518019341347],
  [0.0016085762056007283, 0.023035456520173463, 0.13584185781575728, 0.3298769776932236, 0.3298769776932236, 0.13584185781575728, 0.023035456520173463, 0.0016085762056007283],
  [0.003906250000000001, 0.05593906693299829, 0.3298769776932236, 0.8010698775896221, 0.8010698775896221, 0.3298769776932236, 0.05593906693299829, 0.003906250000000001],
  [0.003906250000000001, 0.05593906693299829, 0.3298769776932236, 0.8010698775896221, 0.8010698775896221, 0.3298769776932236, 0.05593906693299829, 0.003906250000000001],
  [0.0016085762056007283, 0.023035456520173463, 0.13584185781575728, 0.3298769776932236, 0.3298769776932236, 0.13584185781575728, 0.023035456520173463, 0.0016085762056007283],
  [0.00027277518019341347, 0.003906250000000001, 0.023035456520173463, 0.05593906693299829, 0.05593906693299829, 0.023035456520173463, 0.003906250000000001, 0.00027277518019341347],
  [1.9048012525964537e-05, 0.00027277518019341347, 0.0016085762056007283, 0.003906250000000001, 0.003906250000000001, 0.0016085762056007283, 0.00027277518019341347, 1.9048012525964537e-05]],
 [[0.06606362753508628, 0.12851422833200837, 0.2002674693974055, 0.25, 0.25, 0.2002674693974055, 0.12851422833200837, 0.06606362753508628],
  [0.12851422833200837, 0.25, 0.38958228983024995, 0.48632747370614277, 0.48632747370614277, 0.38958228983024995, 0.25, 0.12851422833200837],
  [0.2002674693974055, 0.38958228983024995, 0.6070974421975235, 0.7578582832551991, 0.7578582832551991, 0.6070974421975235, 0.38958228983024995, 0.2002674693974055],
  [0.25, 0.48632747370614277, 0.7578582832551991, 0.9460576467255959, 0.9460576467255959, 0.7578582832551991, 0.48632747370614277, 0.25],
  [0.25, 0.48632747370614277, 0.7578582832551991, 0.9460576467255959, 0.9460576467255959, 0.7578582832551991, 0.48632747370614277, 0.25],
  [0.2002674693974055, 0.38958228983024995, 0.6070974421975235, 0.7578582832551991, 0.7578582832551991, 0.6070974421975235, 0.38958228983024995, 0.2002674693974055],
  [0.12851422833200837, 0.25, 0.38958228983024995, 0.48632747370614277, 0.48632747370614277, 0.38958228983024995, 0.25, 0.12851422833200837],
  [0.06606362753508628, 0.12851422833200837, 0.2002674693974055, 0.25, 0.25, 0.2002674693974055, 0.12851422833200837, 0.06606362753508628]],
 [[0.06606362753508628, 0.12851422833200837, 0.2002674693974055, 0.25, 0.25, 0.2002674693974055, 0.12851422833200837, 0.06606362753508628],
  [0.12851422833200837, 0.25, 0.38958228983024995, 0.48632747370614277, 0.48632747370614277, 0.38958228983024995, 0.25, 0.12851422833200837],
  [0.2002674693974055, 0.38958228983024995, 0.6070974421975235, 0.7578582832551991, 0.7578582832551991, 0.6070974421975235, 0.38958228983024995, 0.2002674693974055],
  [0.25, 0.48632747370614277, 0.7578582832551991, 0.9460576467255959, 0.9460576467255959, 0.7578582832551991, 0.48632747370614277, 0.25],
  [0.25, 0.48632747370614277, 0.7578582832551991, 0.9460576467255959, 0.9460576467255959, 0.7578582832551991, 0.48632747370614277, 0.25],
  [0.2002674693974055, 0.38958228983024995, 0.6070974421975235, 0.7578582832551991, 0.7578582832551991, 0.6070974421975235, 0.38958228983024995, 0.2002674693974055],
  [0.12851422833200837, 0.25, 0.38958228983024995, 0.48632747370614277, 0.48632747370614277, 0.38958228983024995, 0.25, 0.12851422833200837],
  [0.06606362753508628, 0.12851422833200837, 0.2002674693974055, 0.25, 0.25, 0.2002674693974055, 0.12851422833200837, 0.06606362753508628]],
 [[1.9048012525964537e-05, 0.00027277518019341347, 0.0016085762056007283, 0.003906250000000001, 0.003906250000000001, 0.0016085762056007283, 0.00027277518019341347, 1.9048012525964537e-05],
  [0.00027277518019341347, 0.003906250000000001, 0.023035456520173463, 0.05593906693299829, 0.05593906693299829, 0.023035456520173463, 0.003906250000000001, 0.00027277518019341347],
  [0.0016085762056007283, 0.023035456520173463, 0.13584185781575728, 0.3298769776932236, 0.3298769776932236, 0.13584185781575728, 0.023035456520173463, 0.0016085762056007283],
  [0.003906250000000001, 0.05593906693299829, 0.3298769776932236, 0.8010698775896221, 0.8010698775896221, 0.3298769776932236, 0.05593906693299829, 0.003906250000000001],
  [0.003906250000000001, 0.05593906693299829, 0.3298769776932236, 0.8010698775896221, 0.8010698775896221, 0.3298769776932236, 0.05593906693299829, 0.003906250000000001],
  [0.0016085762056007283, 0.023035456520173463, 0.13584185781575728, 0.3298769776932236, 0.3298769776932236, 0.13584185781575728, 0.023035456520173463, 0.0016085762056007283],
  [0.00027277518019341347, 0.003906250000000001, 0.023035456520173463, 0.05593906693299829, 0.05593906693299829, 0.023035456520173463, 0.003906250000000001, 0.00027277518019341347],
  [1.9048012525964537e-05, 0.00027277518019341347, 0.0016085762056007283, 0.003906250000000001, 0.003906250000000001, 0.0016085762056007283, 0.00027277518019341347, 1.9048012525964537e-05]],
 [[2.3969653332244417e-11, 9.562268089971774e-09, 5.1819556356719e-07, 3.814697265625008e-06, 3.814697265625008e-06, 5.1819556356719e-07, 9.562268089971774e-09, 2.3969653332244417e-11],
  [9.562268089971774e-09, 3.814697265625008e-06, 0.0002067249297760079, 0.0015218058196494156, 0.0015218058196494156, 0.0002067249297760079, 3.814697265625008e-06, 9.562268089971774e-09],
  [5.1819556356719e-07, 0.0002067249297760079, 0.011202775375123661, 0.0824692444233059, 0.0824692444233059, 0.011202775375123661, 0.0002067249297760079, 5.1819556356719e-07],
  [3.814697265625008e-06, 0.0015218058196494156, 0.0824692444233059, 0.6070974421975235, 0.6070974421975235, 0.0824692444233059, 0.0015218058196494156, 3.814697265625008e-06],
  [3.814697265625008e-06, 0.0015218058196494156, 0.0824692444233059, 0.6070974421975235, 0.6070974421975235, 0.0824692444233059, 0.0015218058196494156, 3.814697265625008e-06],
  [5.1819556356719e-07, 0.0002067249297760079, 0.011202775375123661, 0.0824692444233059, 0.0824692444233059, 0.011202775375123661, 0.0002067249297760079, 5.1819556356719e-07],
  [9.562268089971774e-09, 3.814697265625008e-06, 0.0002067249297760079, 0.0015218058196494156, 0.0015218058196494156, 0.0002067249297760079, 3.814697265625008e-06, 9.562268089971774e-09],
  [2.3969653332244417e-11, 9.562268089971774e-09, 5.1819556356719e-07, 3.814697265625008e-06, 3.814697265625008e-06, 5.1819556356719e-07, 9.562268089971774e-09, 2.3969653332244417e-11]],
 [[1.3164327314818958e-19, 5.536297320393433e-15, 6.6952463430416106e-12, 2.328306436538698e-10, 2.328306436538698e-10, 6.6952463430416106e-12, 5.536297320393433e-15, 1.3164327314818958e-19],
  [5.536297320393433e-15, 2.328306436538698e-10, 2.8157059226740155e-07, 9.791762524131055e-06, 9.791762524131055e-06, 2.8157059226740155e-07, 2.328306436538698e-10, 5.536297320393433e-15],
  [6.6952463430416106e-12, 2.8157059226740155e-07, 0.00034051359041757954, 0.01184153567586249, 0.01184153567586249, 0.00034051359041757954, 2.8157059226740155e-07, 6.6952463430416106e-12],
  [2.328306436538698e-10, 9.791762524131055e-06, 0.01184153567586249, 0.41179550863378656, 0.41179550863378656, 0.01184153567586249, 9.791762524131055e-06, 2.328306436538698e-10],
  [2.328306436538698e-10, 9.791762524131055e-06, 0.01184153567586249, 0.41179550863378656, 0.41179550863378656, 0.01184153567586249, 9.791762524131055e-06, 2.328306436538698e-10],
  [6.6952463430416106e-12, 2.8157059226740155e-07, 0.00034051359041757954, 0.01184153567586249, 0.01184153567586249, 0.00034051359041757954, 2.8157059226740155e-07, 6.6952463430416106e-12],
  [5.536297320393433e-15, 2.328306436538698e-10, 2.8157059226740155e-07, 9.791762524131055e-06, 9.791762524131055e-06, 2.8157059226740155e-07, 2.328306436538698e-10, 5.536297320393433e-15],
  [1.3164327314818958e-19, 5.536297320393433e-15, 6.6952463430416106e-12, 2.328306436538698e-10, 2.328306436538698e-10, 6.6952463430416106e-12, 5.536297320393433e-15, 1.3164327314818958e-19]],
 [[3.1554436208840535e-30, 5.2939559203394e-23, 3.4694469519536088e-18, 8.881784197001244e-16, 8.881784197001244e-16, 3.4694469519536088e-18, 5.2939559203394e-23, 3.1554436208840535e-30],
  [5.2939559203394e-23, 8.881784197001244e-16, 5.820766091346745e-11, 1.4901161193847676e-08, 1.4901161193847676e-08, 5.820766091346745e-11, 8.881784197001244e-16, 5.2939559203394e-23],
  [3.4694469519536088e-18, 5.820766091346745e-11, 3.814697265625001e-06, 0.0009765625, 0.0009765625, 3.814697265625001e-06, 5.820766091346745e-11, 3.4694469519536088e-18],
  [8.881784197001244e-16, 1.4901161193847676e-08, 0.0009765625, 0.25, 0.25, 0.0009765625, 1.4901161193847676e-08, 8.881784197001244e-16],
  [8.881784197001244e-16, 1.4901161193847676e-08, 0.0009765625, 0.25, 0.25, 0.0009765625, 1.4901161193847676e-08, 8.881784197001244e-16],
  [3.4694469519536088e-18, 5.820766091346745e-11, 3.814697265625001e-06, 0.0009765625, 0.0009765625, 3.814697265625001e-06, 5.820766091346745e-11, 3.4694469519536088e-18],
  [5.2939559203394e-23, 8.881784197001244e-16, 5.820766091346745e-11, 1.4901161193847676e-08, 1.4901161193847676e-08, 5.820766091346745e-11, 8.881784197001244e-16, 5.2939559203394e-23],
  [3.1554436208840535e-30, 5.2939559203394e-23, 3.4694469519536088e-18, 8.881784197001244e-16, 8.881784197001244e-16, 3.4694469519536088e-18, 5.2939559203394e-23, 3.1554436208840535e-30]],
 [[3.3010113067809964e-43, 8.360719670133873e-33, 7.21065575178869e-26, 2.117582368135768e-22, 2.117582368135768e-22, 7.21065575178869e-26, 8.360719670133873e-33, 3.3010113067809964e-43],
  [8.360719670133873e-33, 2.117582368135768e-22, 1.8262970276624776e-15, 5.363360168452738e-12, 5.363360168452738e-12, 1.8262970276624776e-15, 2.117582368135768e-22, 8.360719670133873e-33],
  [7.21065575178869e-26, 1.8262970276624776e-15, 1.5750796207210184e-08, 4.6255998733837856e-05, 4.6255998733837856e-05, 1.5750796207210184e-08, 1.8262970276624776e-15, 7.21065575178869e-26],
  [2.117582368135768e-22, 5.363360168452738e-12, 4.6255998733837856e-05, 0.1358418578157573, 0.1358418578157573, 4.6255998733837856e-05, 5.363360168452738e-12, 2.117582368135768e-22],
  [2.117582368135768e-22, 5.363360168452738e-12, 4.6255998733837856e-05, 0.1358418578157573, 0.1358418578157573, 4.6255998733837856e-05, 5.363360168452738e-12, 2.117582368135768e-22],
  [7.21065575178869e-26, 1.8262970276624776e-15, 1.5750796207210184e-08, 4.6255998733837856e-05, 4.6255998733837856e-05, 1.5750796207210184e-08, 1.8262970276624776e-15, 7.21065575178869e-26],
  [8.360719670133873e-33, 2.117582368135768e-22, 1.8262970276624776e-15, 5.363360168452738e-12, 5.363360168452738e-12, 1.8262970276624776e-15, 2.117582368135768e-22, 8.360719670133873e-33],
  [3.3010113067809964e-43, 8.360719670133873e-33, 7.21065575178869e-26, 2.117582368135768e-22, 2.117582368135768e-22, 7.21065575178869e-26, 8.360719670133873e-33, 3.3010113067809964e-43]],
 [[1.5071567844635535e-58, 2.1807678146028544e-44, 6.010492961557393e-35, 3.1554436208840535e-30, 3.1554436208840535e-30, 6.010492961557393e-35, 2.1807678146028544e-44, 1.5071567844635535e-58],
  [2.1807678146028544e-44, 3.1554436208840535e-30, 8.696832164761637e-21, 4.565742569156177e-16, 4.565742569156177e-16, 8.696832164761637e-21, 3.1554436208840535e-30, 2.1807678146028544e-44],
  [6.010492961557393e-35, 8.696832164761637e-21, 2.3969653332244333e-11, 1.2583808047989792e-06, 1.2583808047989792e-06, 2.3969653332244333e-11, 8.696832164761637e-21, 6.010492961557393e-35],
  [3.1554436208840535e-30, 4.565742569156177e-16, 1.2583808047989792e-06, 0.06606362753508628, 0.06606362753508628, 1.2583808047989792e-06, 4.565742569156177e-16, 3.1554436208840535e-30],
  [3.1554436208840535e-30, 4.565742569156177e-16, 1.2583808047989792e-06, 0.06606362753508628, 0.06606362753508628, 1.2583808047989792e-06, 4.565742569156177e-16, 3.1554436208840535e-30],
  [6.010492961557393e-35, 8.696832164761637e-21, 2.3969653332244333e-11, 1.2583808047989792e-06, 1.2583808047989792e-06, 2.3969653332244333e-11, 8.696832164761637e-21, 6.010492961557393e-35],
  [2.1807678146028544e-44, 3.1554436208840535e-30, 8.696832164761637e-21, 4.565742569156177e-16, 4.565742569156177e-16, 8.696832164761637e-21, 3.1554436208840535e-30, 2.1807678146028544e-44],
  [1.5071567844635535e-58, 2.1807678146028544e-44, 6.010492961557393e-35, 3.1554436208840535e-30, 3.1554436208840535e-30, 6.010492961557393e-35, 2.1807678146028544e-44, 1.5071567844635535e-58]],
 [[3.003272143191179e-76, 9.394585459592318e-58, 2.009399286955082e-45, 2.938735877055727e-39, 2.938735877055727e-39, 2.009399286955082e-45, 9.394585459592318e-58, 3.003272143191179e-76],
  [9.394585459592318e-58, 2.938735877055727e-39, 6.285635275025237e-27, 9.192708493887553e-21, 9.192708493887553e-21, 6.285635275025237e-27, 2.938735877055727e-39, 9.394585459592318e-58],
  [2.009399286955082e-45, 6.285635275025237e-27, 1.3444287769823358e-14, 1.9662200074984073e-08, 1.9662200074984073e-08, 1.3444287769823358e-14, 6.285635275025237e-27, 2.009399286955082e-45],
  [2.938735877055727e-39, 9.192708493887553e-21, 1.9662200074984073e-08, 0.028755864082027342, 0.028755864082027342, 1.9662200074984073e-08, 9.192708493887553e-21, 2.938735877055727e-39],
  [2.938735877055727e-39, 9.192708493887553e-21, 1.9662200074984073e-08, 0.028755864082027342, 0.028755864082027342, 1.9662200074984073e-08, 9.192708493887553e-21, 2.938735877055727e-39],
  [2.009399286955082e-45, 6.285635275025237e-27, 1.3444287769823358e-14, 1.9662200074984073e-08, 1.9662200074984073e-08, 1.3444287769823358e-14, 6.285635275025237e-27, 2.009399286955082e-45],
  [9.394585459592318e-58, 2.938735877055727e-39, 6.285635275025237e-27, 9.192708493887553e-21, 9.192708493887553e-21, 6.285635275025237e-27, 2.938735877055727e-39, 9.394585459592318e-58],
  [3.003272143191179e-76, 9.394585459592318e-58, 2.009399286955082e-45, 2.938735877055727e-39, 2.938735877055727e-39, 2.009399286955082e-45, 9.394585459592318e-58, 3.003272143191179e-76]],
 [[2.6118953774438405e-96, 6.684181585222283e-73, 2.694283024543055e-57, 1.7105694144590234e-49, 1.7105694144590234e-49, 2.694283024543055e-57, 6.684181585222283e-73, 2.6118953774438405e-96],
  [6.684181585222283e-73, 1.7105694144590234e-49, 6.895022340310091e-34, 4.377570663477814e-26, 4.377570663477814e-26, 6.895022340310091e-34, 1.7105694144590234e-49, 6.684181585222283e-73],
  [2.694283024543055e-57, 6.895022340310091e-34, 2.7792694451051804e-18, 1.764526318887254e-10, 1.764526318887254e-10, 2.7792694451051804e-18, 6.895022340310091e-34, 2.694283024543055e-57],
  [1.7105694144590234e-49, 4.377570663477814e-26, 1.764526318887254e-10, 0.011202775375123661, 0.011202775375123661, 1.764526318887254e-10, 4.377570663477814e-26, 1.7105694144590234e-49],
  [1.7105694144590234e-49, 4.377570663477814e-26, 1.764526318887254e-10, 0.011202775375123661, 0.011202775375123661, 1.764526318887254e-10, 4.377570663477814e-26, 1.7105694144590234e-49],
  [2.694283024543055e-57, 6.895022340310091e-34, 2.7792694451051804e-18, 1.764526318887254e-10, 1.764526318887254e-10, 2.7792694451051804e-18, 6.895022340310091e-34, 2.694283024543055e-57],
  [6.684181585222283e-73, 1.7105694144590234e-49, 6.895022340310091e-34, 4.377570663477814e-26, 4.377570663477814e-26, 6.895022340310091e-34, 1.7105694144590234e-49, 6.684181585222283e-73],
  [2.6118953774438405e-96, 6.684181585222283e-73, 2.694283024543055e-57, 1.7105694144590234e-49, 1.7105694144590234e-49, 2.694283024543055e-57, 6.684181585222283e-73, 2.6118953774438405e-96]]
 ]
