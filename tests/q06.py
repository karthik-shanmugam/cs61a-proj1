test = {
  'names': [
    'q06',
    'q6',
    '6'
  ],
  'params': {
    'doctest': {
      'setup': """
      
      """,
      'teardown': """
      
      """
    }
  },
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(3, 1, 5, 6)
        >>> averaged_dice = make_averaged(dice, 1000)
        >>> averaged_dice()  # average of calling dice 1000 times
        0e5bf441e74f6ece1ca90671e8d73f50
        # locked
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> dice = make_test_dice(3, 1, 5, 6)
        >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
        >>> averaged_roll_dice(2, dice)
        6.0
        """,
        'type': 'doctest'
      }
    ]
  ]
}