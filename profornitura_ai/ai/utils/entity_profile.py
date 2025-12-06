from typing import Optional
import frappe
from ..config import EntityProfile, DEFAULT_ENTITY

def load_entity_profile(entity_name: Optional[str] = None) -> EntityProfile:
    if not entity_name:
        return DEFAULT_ENTITY

    try:
        doc = frappe.get_doc("Entity Profile", entity_name)
        return EntityProfile(
            name=doc.name,
            entity_type=doc.entity_type,
            years_active=doc.years_active or 0,
            is_startup=bool(doc.is_startup),
            zero_liquidity_mode=bool(doc.zero_liquidity_mode),
            max_risk_score=float(getattr(doc, "max_risk_score", DEFAULT_ENTITY.max_risk_score)),
        )
    except Exception:
        return DEFAULT_ENTITY
