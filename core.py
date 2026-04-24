import json
import logging

class RobloxError(Exception):
    pass

class InvalidInputError(RobloxError):
    pass

logging.basicConfig(level=logging.INFO)

class RobloxTools:
    def __init__(self, game_data):
        self.game_data = game_data

    def fetch_game_info(self, game_id):
        try:
            if not isinstance(game_id, int):
                raise InvalidInputError('Game ID must be an integer.')

            game_info = self.game_data.get(game_id)
            if not game_info:
                raise RobloxError('Game not found.')

            return json.dumps(game_info)

        except InvalidInputError as e:
            logging.error(f'Invalid Input: {e}')
            return json.dumps({'error': str(e)})
        except RobloxError as e:
            logging.error(f'Roblox Error: {e}')
            return json.dumps({'error': str(e)})
        except Exception as e:
            logging.exception('An unexpected error occurred.')
            return json.dumps({'error': 'An unexpected error occurred.'})

# Sample game data for simulation
sample_game_data = {
    123: {'name': 'Fun Obby', 'players': 42},
    456: {'name': 'Epic Simulator', 'players': 75}
}

# Example of using the RobloxTools class
if __name__ == '__main__':
    tools = RobloxTools(sample_game_data)
    print(tools.fetch_game_info(123))  # Should return game info
    print(tools.fetch_game_info('abc'))  # Should log an error and return an error JSON
    print(tools.fetch_game_info(999))  # Should log 'Game not found' error and return an error JSON