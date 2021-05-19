class Mediator:
    ALL_GAMEOBJECTS = []
    TO_BE_REMOVED = []
    COLLISIONS = []
    PARTICLES = []
    ALL_WALLS = []
    CURRENT_WALLS = []

    def collisions(self):

        for g_object in Mediator.ALL_GAMEOBJECTS:            
            for g2_object in Mediator.ALL_GAMEOBJECTS:

                if not g_object.get_id() == g2_object.get_id() :

                    #if not g_object.get_id() == 'player' and g2_object.get_id() == 'player_bullet':

                        if g_object.get_rect().colliderect(g2_object.get_rect()):
                            #print("i " + str(g_object.get_id()) + " collide with " + str(g2_object.get_id()))
                            #g_object.collision_ids.append(str(g2_object.get_id()))
                            #g_object.collision_vels.append(g2_object.vel.copy())
                            #Mediator.COLLISIONS.append(g_object)

                            g2_object.collision_ids.append(str(g_object.get_id()))
                            g2_object.collision_vels.append(g_object.vel.copy())
                            Mediator.COLLISIONS.append(g2_object)
        
    def get_walls_to_render(self, player_rect):
        
        for wall in Mediator.ALL_WALLS:
            if player_rect.x - wall.rect.x >= -1024 and player_rect.x - wall.rect.x <= 1024:
                if player_rect.y - wall.rect.y >= -1024 and player_rect.y - wall.rect.y <= 1024:
                    Mediator.CURRENT_WALLS.append(wall)