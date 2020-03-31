value1 = 1:100;
%value should be range 1-million but wont compute
value2 = 1:55;
%value should be range 1-555710 but wont compute
value3 = 1:47;
%value should be range 1-470400 but wont compute
ctrl = 1;
ctrl2 = 0.55071;
ctrl3 = 0.47041;
bid = 1000000;
bid2 = 555710;
bid3 = 470400;

 for n1 = 1:length(value1)
     for n2 = 1:length(value2)
         for n3 = 1:length(value3)
             temp_eq=1;
             strategy1 = n1;
             strategy2 = n2;
             strategy3 = n3;
             utility1 = 0;
             utility2 = 0;
             utility3 = 0;
            if (strategy1 > strategy2)
                if(strategy1 > strategy3)
                    temp_high = strategy1;
                    if(strategy2 > strategy3)
                        temp_second_high = strategy2;
                    else
                        temp_second_high = strategy3;
                    end
                else
                    temp_high=strategy3;
                    temp_second_high=strategy1;
                end
            elseif(strategy2>strategy3)
                temp_high=strategy2;
                if(strategy3>strategy1)
                    temp_second_high=strategy3;
                else
                    temp_second_high=strategy1;
                end
            else
                temp_high=strategy3;
                temp_second_high=strategy2;    
            end
            utility1 = ctrl*(temp_high-temp_second_high);
            utility2 = ctrl2*(temp_high-temp_second_high);
            utility3 = ctrl3*(temp_high-temp_second_high);
            
            for temp_n1 = 1:length(value1)
                if (temp_n1 ~= strategy1)
                    if (temp_n1 > strategy2)
                        if(temp_n1 > strategy3)
                            temp_high = temp_n1;
                            if(strategy2 > strategy3)
                                temp_second_high = strategy2;
                            else
                                temp_second_high = strategy3;
                            end
                        else
                            temp_high=strategy3;
                            temp_second_high=temp_n1;
                        end
                    elseif(strategy2>strategy3)
                        temp_high=strategy2;
                        if(strategy3>temp_n1)
                            temp_second_high=strategy3;
                        else
                            temp_second_high=temp_n1;
                        end
                    else
                        temp_high=strategy3;
                        temp_second_high=strategy2;    
                    end
                end
                temp_utility1 = ctrl*(temp_high-temp_second_high); 
                if(utility1 < temp_utility1)
                    temp_eq=0;
                end
            end
            
            for temp_n2 = 1:length(value2)
                 if (temp_n2 ~= strategy2)
                    if (strategy1 > temp_n2)
                        if(strategy1 > strategy3)
                            temp_high = strategy1;
                            if(temp_n2 > strategy3)
                                temp_second_high = temp_n2;
                            else
                                temp_second_high = strategy3;
                            end
                        else
                            temp_high=strategy3;
                            temp_second_high=strategy1;
                        end
                    elseif(temp_n2>strategy3)
                        temp_high=temp_n2;
                        if(strategy3>strategy1)
                            temp_second_high=strategy3;
                        else
                            temp_second_high=strategy1;
                        end
                    else
                        temp_high=strategy3;
                        temp_second_high=temp_n2;    
                    end
                    temp_utility2 = ctrl2*(temp_high-temp_second_high);
                    if(utility2 < temp_utility2)
                        temp_eq=0;
                    end
                  end
            end
            
            for temp_n3 = 1:length(value3)
                if (temp_n3 ~= strategy3)
                    if (strategy1 > strategy2)
                        if(strategy1 > temp_n3)
                            temp_high = strategy1;
                            if(temp_n2 > temp_n3)
                                temp_second_high = strategy2;
                            else
                                temp_second_high = temp_n3;
                            end
                        else
                            temp_high=temp_n3;
                            temp_second_high=strategy1;
                        end
                    elseif(strategy2>temp_n3)
                        temp_high=strategy2;
                        if(temp_n3>strategy1)
                            temp_second_high=temp_n3;
                        else
                            temp_second_high=strategy1;
                        end
                    else
                        temp_high=temp_n3;
                        temp_second_high=strategy2;
                    end
                      
                        temp_utility3 = ctrl3*(temp_high-temp_second_high);
                    if(utility3 < temp_utility3)
                        temp_eq=0;
                    end
                     
                end
                
            end
            
            
            if temp_eq==1
                eq_1 = strategy1;
                eq_2 = strategy2;
                eq_3 = strategy3;
            end

         end
     end
 end
 
   
             
                

             
             