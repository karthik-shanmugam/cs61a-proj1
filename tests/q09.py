test = {
  'names': [
    'q09',
    '9',
    'q9'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        25f2000bcc4be0364767b44f9895f1cd
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        25f2000bcc4be0364767b44f9895f1cd
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        21a3b3b0c92a1455674c51aff6000790
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}