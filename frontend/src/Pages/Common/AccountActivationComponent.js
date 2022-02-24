import {Container, Row} from "react-bootstrap";
import React, {useEffect, useState} from "react";
import {accountActivationAction} from "../../Redux/ActionCreators";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router-dom";
import {set} from "../../Services/Storage";

export default function AccountActivationComponent(props){
    const [success,setSuccess] = useState(null);
    const [globalMessage, setGlobalMessage] = useState("");
    const [seconds, setSeconds] = useState(10);
    const dispatch = useDispatch();
    const history = useHistory();

    useEffect(() => {
        let params = props.match.params;
        if((params.type_account ==="reader" || params.type_account==="publisher")
         && params.activation_token){
            const data = {
                "token": params.activation_token,
                "type": params.type_account,
            };
            dispatch(accountActivationAction((data)))
                .then(data => {
                    setSuccess(data.payload.Success);
                    setGlobalMessage(data.payload.message);
                })
                .catch(err => {
                    console.log("err", err);
                    setGlobalMessage("Erreur");
                });
        }
    }, []);
    useEffect(()=>{
        if(success){
            if( seconds > 0){
                setTimeout(() => setSeconds(seconds -1),1000);
            }else{
                history.push("/login")
            }
        }
    });

    return(
        <div>
            <div>
                <Row>
                    <div>
                        <Container>
                            {success ?
                            <>
                                <p>
                                    Your account is Activated
                                </p>
                                <p>You will be redirected to the login page in : </p>
                                <div>{seconds}</div>
                            </>
                            :null
                            }
                        </Container>
                    </div>
                </Row>
            </div>
        </div>
    );
}