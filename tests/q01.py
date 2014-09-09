test = {
  'names': [
    'q01',
    '1',
    'q1'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> roll_dice(2, make_test_dice(4, 6, 1))
        51a99543518af4b96d317545157609b6
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(4, 6, 1))
        7c1693ef096852911594f5e274a4d9fe
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(1, 2, 3))
        7c1693ef096852911594f5e274a4d9fe
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> counted_dice = make_test_dice(4, 1, 2, 6)
        >>> roll_dice(3, counted_dice)
        7c1693ef096852911594f5e274a4d9fe
        # locked
        >>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
        c16e6245873267320a8a306c69243418
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}