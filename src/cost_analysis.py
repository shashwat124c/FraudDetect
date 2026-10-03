"""Cost-benefit and threshold optimization analysis for fraud detection."""

from typing import Dict
import numpy as np


def compute_cost_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    amounts: np.ndarray,
    investigation_cost: float = 15.0,
    fraud_recovery_rate: float = 1.0,
) -> Dict[str, float]:
    """Calculate total financial cost based on detection performance.

    Args:
        y_true: True binary labels (1 = fraud, 0 = non-fraud).
        y_pred: Predicted binary labels.
        amounts: Transaction amounts.
        investigation_cost: Cost to manually investigate a flagged alert (False Positive or True Positive).
        fraud_recovery_rate: Fraction of fraud saved when detected (default 1.0).

    Returns:
        dict: Detailed financial breakdown (false negatives loss, investigation expense, net loss).
    """
    fn_mask = (y_true == 1) & (y_pred == 0)
    fp_mask = (y_true == 0) & (y_pred == 1)
    tp_mask = (y_true == 1) & (y_pred == 1)

    fraud_loss_fn = float(np.sum(amounts[fn_mask]))
    unrecovered_tp = float(np.sum(amounts[tp_mask]) * (1.0 - fraud_recovery_rate))
    investigation_expenses = float((np.sum(fp_mask) + np.sum(tp_mask)) * investigation_cost)

    total_cost = fraud_loss_fn + unrecovered_tp + investigation_expenses

    return {
        "fraud_loss_fn": fraud_loss_fn,
        "investigation_expenses": investigation_expenses,
        "total_financial_loss": total_cost,
        "flagged_count": int(np.sum(y_pred)),
    }
