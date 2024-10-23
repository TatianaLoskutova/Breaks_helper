from django.db.models import Count, OuterRef, Prefetch, Q, Subquery

from breaks import constants
from breaks.models.breaks import Break
from breaks.models.replacements import Replacement, ReplacementMember


class ReplacementFactory:
    model = Replacement

    def list(self):
        all_statuses = constants.BREAK_ALL_STATUSES
        annotates_stats = dict()
        for status in all_statuses:
            annotates_stats[f'{status}_pax'] = Count(
                'breaks', distinct=True, filter=Q(breaks__status_id=status),
            )

        qs = self.model.objects.prefetch_related(
            'group',
            'group__group__manager',
            'group__group__manager__user',
            'group__group__organisation',
            'members',
            'members__employee',
            'members__employee__user',
        ).annotate(
            all_pax=Count('breaks', distinct=True),
        ).annotate(**annotates_stats)
        return qs


# class ReplacementFactory:
#     model = Replacement

#     def list(self):
#         break_subquery = Break.objects.filter(
#                 member=OuterRef('id'),
#                 replacement=OuterRef('replacement'),
#             )

#         members_qs = ReplacementMember.objects.annotate(
#             break_start=Subquery(break_subquery.values('break_start')[:1]),
#             break_end=Subquery(break_subquery.values('break_end')[:1]),
#         ).select_related(
#             'member__employee',
#             'member__employee__user',
#             'status',
#         )
#         qs = self.model.objects.prefetch_related(
#             'group',
#             'group__group__manager',
#             'group__group__manager__user',
#             'group__group__organisation',
#             Prefetch(
#                 lookup='members_info',
#                 queryset=members_qs,
#             )
#         )
#         return qs
