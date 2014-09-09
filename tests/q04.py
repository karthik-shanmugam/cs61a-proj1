test = {
  'names': [
    'q04',
    '4',
    'q4'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(1, 1, goal=100) # start can be 0 or 1
        >>> score0
        2d851ed82915abfbfde3501bc8dce2be
        # locked
        >>> score1
        2d851ed82915abfbfde3501bc8dce2be
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(2, 7, goal=100)
        >>> score0
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        >>> score1
        51a99543518af4b96d317545157609b6
        # locked
        >>> start
        7c1693ef096852911594f5e274a4d9fe
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(8, 3, goal=100)
        >>> score0
        51a99543518af4b96d317545157609b6
        # locked
        >>> score1
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        >>> start
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(4, 3, goal=100)
        >>> score0
        c5ac6cf9239bd60113b8ac9c67cd7c49
        # locked
        >>> score1
        21a3b3b0c92a1455674c51aff6000790
        # locked
        >>> start
        df27d1337f030610fbbf8afc5bfcfde0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(3, 4, goal=100)
        >>> score0
        21a3b3b0c92a1455674c51aff6000790
        # locked
        >>> score1
        c5ac6cf9239bd60113b8ac9c67cd7c49
        # locked
        >>> start
        7c1693ef096852911594f5e274a4d9fe
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}