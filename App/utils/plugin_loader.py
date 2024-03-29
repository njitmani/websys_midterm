import os
import importlib
from logging import getLogger
from ..strategies.base_strategy import OperationStrategy

def load_plugins(logger=None):
    if logger is None:
        logger = getLogger(__name__)

    plugins = {}
    plugins_dir = os.path.join(os.path.dirname(__file__), '..', 'plugins')
    if not os.path.exists(plugins_dir):
        logger.warning("Plugins directory does not exist.")
        return plugins

    for module in os.listdir(plugins_dir):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        module_name = module[:-3]
        try:
            module_path = f'App.plugins.{module_name}'
            plugin_module = importlib.import_module(module_path, package='src')
            for item in dir(plugin_module):
                obj = getattr(plugin_module, item)
                if isinstance(obj, type) and issubclass(obj, OperationStrategy) and obj is not OperationStrategy:
                    plugin_name = obj.__name__
                    plugins[plugin_name.lower()] = obj()
                    logger.info(f"Loaded plugin: {plugin_name}")
        except Exception as e:
            logger.error(f"Failed to load plugin {module_name}: {e}")

    return plugins