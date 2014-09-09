test = {
  'names': [
    'q00',
    '0',
    'q0'
  ],
  'points': 0,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> test_dice = make_test_dice(4, 1, 2)
        >>> test_dice()
        21a3b3b0c92a1455674c51aff6000790
        # locked
        >>> test_dice() # Second call
        7c1693ef096852911594f5e274a4d9fe
        # locked
        >>> test_dice() # Third call
        7664e893bf315e09408e5d39d70544c8
        # locked
        >>> test_dice() # Fourth call
        21a3b3b0c92a1455674c51aff6000790
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}