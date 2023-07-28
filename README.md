# Measuring Central Bank Policy Uncertainty

[![pypi-image]][pypi-url]
[![version-image]][release-url]
[![release-date-image]][release-url]
[![license-image]][license-url]
[![codecov][codecov-image]][codecov-url]
[![jupyter-book-image]][docs-url]

<!-- Links: -->
[codecov-image]: https://codecov.io/gh/entelecheia/nbcpu/branch/main/graph/badge.svg?token=P414TXNSHY
[codecov-url]: https://codecov.io/gh/entelecheia/nbcpu
[pypi-image]: https://img.shields.io/pypi/v/nbcpu
[license-image]: https://img.shields.io/github/license/entelecheia/nbcpu
[license-url]: https://github.com/entelecheia/nbcpu/blob/main/LICENSE
[version-image]: https://img.shields.io/github/v/release/entelecheia/nbcpu?sort=semver
[release-date-image]: https://img.shields.io/github/release-date/entelecheia/nbcpu
[release-url]: https://github.com/entelecheia/nbcpu/releases
[jupyter-book-image]: https://jupyterbook.org/en/stable/_images/badge.svg

[repo-url]: https://github.com/entelecheia/nbcpu
[pypi-url]: https://pypi.org/project/nbcpu
[docs-url]: https://nbcpu.entelecheia.ai
[changelog]: https://github.com/entelecheia/nbcpu/blob/main/CHANGELOG.md
[contributing guidelines]: https://github.com/entelecheia/nbcpu/blob/main/CONTRIBUTING.md
<!-- Links: -->

Quantifying Central Bank Policy Uncertainty in a Highly Dollarized Economy: A Topic Modeling Approach

- Documentation: [https://nbcpu.entelecheia.ai][docs-url]
- GitHub: [https://github.com/entelecheia/nbcpu][repo-url]
- PyPI: [https://pypi.org/project/nbcpu][pypi-url]

Understanding and measuring central bank policy uncertainty are fundamental to predicting economic outcomes, particularly in economies like Cambodia where the monetary policy tools are underdeveloped and the economy is heavily dollarized. This study aims to develop and evaluate topic-based measures of policy uncertainty in the Cambodian context, using narrative text data derived from major news media outlets. Leveraging Latent Dirichlet Allocation (LDA), a widely-used generative model for text data, we estimate the document-topic and topic-word distributions from a corpus of news articles, thereby deriving measures of policy uncertainty.

Our methodology involves applying two topic models: one classifies articles into four categories of interest - Exchange Rate Policy Uncertainty, Currency Stabilization Policy Uncertainty, De-dollarization Policy Uncertainty, and International Monetary Policy Impact Uncertainty; the other quantifies the intensity of uncertainty within these articles. We use a seed word approach to guide the LDA in determining relevant topics and the level of associated uncertainty.

The effectiveness of these measures is evaluated via a narrative approach, analyzing articles with high uncertainty scores, and through comparison with established policy uncertainty indices. The proposed methodology and findings offer valuable insights for central banks and policymakers in dollarized economies, like Cambodia, enhancing their communication strategies to effectively manage policy uncertainty and its economic implications.


## Changelog

See the [CHANGELOG] for more information.

## Contributing

Contributions are welcome! Please see the [contributing guidelines] for more information.

## License

This project is released under the [MIT License][license-url].
