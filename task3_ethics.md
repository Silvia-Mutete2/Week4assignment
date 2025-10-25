# Ethical Reflection — Task 3

This project builds a small predictive model using synthetic data to demonstrate end-to-end workflow. Even at this scale, several ethical considerations apply:

- Data provenance and consent: For real datasets we must ensure subjects gave informed consent for use, and that data collection aligns with legal and institutional policies. Synthetic data avoids some privacy risks, but is not a substitute for careful governance when using real records.

- Bias and fairness: Models can learn and amplify biases present in training data. Before deployment, practitioners should check performance across demographic slices, consider rebalancing or fairness-aware methods, and avoid using downstream decisions that unjustly harm groups.

- Transparency and accountability: Maintain clear documentation of data sources, preprocessing steps, and model limitations. Provide explainability where possible and log decisions for auditing.

- Misuse risk: Predictive models can be repurposed in harmful ways. Limit access, apply purpose specifications, and include human oversight on consequential decisions.

These steps help reduce harms and increase trust when moving from demonstration to production.