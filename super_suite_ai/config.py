import dataclasses
from typing import List, Literal

EntityType = Literal["SRL", "DITTA_INDIVIDUALE", "COOPERATIVA", "CONSORZIO"]

@dataclasses.dataclass
class EntityProfile:
    name: str
    entity_type: EntityType
    years_active: int
    is_startup: bool = False
    zero_liquidity_mode: bool = True
    max_risk_score: float = 0.4

@dataclasses.dataclass
class ZeroLiquidityPolicy:
    allow_anticipo_fattura: bool = True
    allow_advance_payment: bool = False
    require_partner_sponsor: bool = True

@dataclasses.dataclass
class GovernancePolicy:
    enforce_anac_checks: bool = True
    enforce_cpv_whitelist: bool = True
    enforce_cig_format: bool = True
    require_dual_approval: bool = True

@dataclasses.dataclass
class AutopilotConfig:
    enable_scheduler: bool = True
    enable_doc_events: bool = True
    dry_run: bool = True
    log_level: str = "INFO"
    enabled_strategies: List[str] = dataclasses.field(
        default_factory=lambda: [
            "ZERO_LIQUIDITY_ENGINE",
            "GOVERNANCE_GUARDIAN",
            "AI_DECISION_BOARD",
            "TIMELINE_AI",
        ]
    )

DEFAULT_ENTITY = EntityProfile(
    name="Profornitura Italia SRL",
    entity_type="SRL",
    years_active=0,
    is_startup=True,
    zero_liquidity_mode=True,
    max_risk_score=0.35,
)

DEFAULT_ZERO_LIQ_POLICY = ZeroLiquidityPolicy()
DEFAULT_GOVERNANCE_POLICY = GovernancePolicy()
DEFAULT_AUTOPILOT_CONFIG = AutopilotConfig()
