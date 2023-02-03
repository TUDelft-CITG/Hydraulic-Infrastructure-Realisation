"""
Module contains DependenciesFromRecordedActivities that inherits from critical_path.base_cp.BaseCP
"""
from openclsim.critical_path.base_cp import BaseCP


class DependenciesFromRecordedActivities(BaseCP):
    """
    Build dependecies from recorded_activities_df
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_dependency_list(self):
        """
        Get dependencies directly from recorded activities (match on identical timestamps)

        Notes
        -----
        this method is likely to provide too many dependencies
        (and hence make too many activities interconnected)

        Returns
        -------
        dependency_list : list
            list of tuples like [(A1, A2), (A1, A3), (A3, A4)]
            where A2 depends on A1 (A1 'causes' A2) et cetera
        """
        # ...
        return []
