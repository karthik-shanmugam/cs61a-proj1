test = {
  'names': [
    'q03',
    '3',
    'q3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> select_dice(4, 24) == six_sided
        b294cbe78799f4f48e6cff6453d18f30
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(16, 64) == six_sided
        069e567af70ba4001b21f37e779a1f36
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(0, 0) == six_sided
        b294cbe78799f4f48e6cff6453d18f30
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(50, 80) == six_sided
        069e567af70ba4001b21f37e779a1f36
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}